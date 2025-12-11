import datetime

from flask import Blueprint, render_template, request, current_app, abort
from . import db
from .models import SearchLog
import requests

main_bp = Blueprint("main", __name__)


# ------------- TheSportsDB helpers (for search + profile) ------------- #

def search_players_api(name: str):
    """Search players via TheSportsDB (API id, name, position, team, thumb)."""
    key = current_app.config.get("THESPORTSDB_API_KEY")
    base = current_app.config.get("THESPORTSDB_BASE_URL")
    url = f"{base}/{key}/searchplayers.php"

    try:
        resp = requests.get(url, params={"p": name}, timeout=5)
        resp.raise_for_status()
    except requests.RequestException as e:
        current_app.logger.error("TheSportsDB API error: %s", e)
        return []

    data = resp.json() or {}
    players = data.get("player") or []

    results = []
    for p in players:
        sport = (p.get("strSport") or "").lower()
        if sport and "football" not in sport:
            continue  # skip soccer etc.

        results.append(
            {
                "api_id": p.get("idPlayer"),
                "name": p.get("strPlayer"),
                "position": p.get("strPosition"),
                "team": p.get("strTeam"),
                "nationality": p.get("strNationality"),
                "thumb": p.get("strThumb"),
                "league": p.get("strLeague"),
            }
        )

    current_app.logger.info(
        "After filtering, %d players from API for %r", len(results), name
    )
    return results


# ------------- Pro-Football-Reference helpers (career stats) ----------- #

def _map_position_for_pfr(position_text: str | None) -> str | None:
    """
    Map TheSportsDB position text to the codes expected by
    pro-football-reference-web-scraper: 'QB', 'RB', 'WR', 'TE'.
    """
    if not position_text:
        return None

    pos = position_text.upper()
    if "QB" in pos or "QUARTERBACK" in pos:
        return "QB"
    if "RB" in pos or "RUNNING" in pos:
        return "RB"
    if "TE" in pos or "TIGHT" in pos:
        return "TE"
    if "WR" in pos or "WIDE" in pos or "RECEIVER" in pos:
        return "WR"
    return None


def get_pfr_career_stats(player_name: str, position_text: str | None):
    """
    Use pro-football-reference-web-scraper to fetch ALL seasons of game logs
    for a player, then aggregate into career totals.

    Returns a dict like:
      {
        "seasons": 10,
        "games": 153,
        "pass_yards": ...,
        "pass_tds": ...,
        "interceptions": ...,
        "rush_yards": ...,
        "rush_tds": ...,
        "receptions": ...,
        "rec_yards": ...,
        "rec_tds": ...,
      }
    or None if we can't get data.
    """
    try:
        from pro_football_reference_web_scraper import player_game_log as p
        import pandas as pd
    except ImportError:
        current_app.logger.warning(
            "pro-football-reference-web-scraper or pandas not installed; "
            "career stats disabled"
        )
        return None

    pos_code = _map_position_for_pfr(position_text)
    if not pos_code:
        current_app.logger.info(
            "No PFR position mapping for %r; skipping stats", position_text
        )
        return None

    frames = []
    played_seasons: set[int] = set()
    current_year = datetime.date.today().year

    # Reasonable window for modern players; adjust if you want older seasons
    for season in range(1990, current_year + 1):
        try:
            df = p.get_player_game_log(
                player=player_name,
                position=pos_code,
                season=season,
            )
        except Exception as e:
            # If the library can't find this player/season, just skip.
            current_app.logger.debug(
                "PFR error for %s (%s, %d): %s",
                player_name, pos_code, season, e,
            )
            continue

        if df is None or getattr(df, "empty", True):
            continue

        df = df.copy()
        df["season"] = season
        frames.append(df)
        played_seasons.add(season)

    if not frames:
        current_app.logger.info(
            "No PFR data found for %s (%s)", player_name, pos_code
        )
        return None

    all_games = pd.concat(frames, ignore_index=True)

    stats: dict[str, int] = {}
    stats["seasons"] = len(played_seasons)
    stats["games"] = int(len(all_games))

    cols = set(all_games.columns)

    def sum_col(col_name: str, key_name: str):
        if col_name in cols:
            try:
                stats[key_name] = int(
                    all_games[col_name].fillna(0).astype(float).sum()
                )
            except Exception:
                current_app.logger.warning(
                    "Could not aggregate column %s for %s",
                    col_name, player_name,
                )

    # Column names from the official docs for each position type:
    # QBs: pass_yds, pass_td, int, rush_att, rush_yds, rush_td
    sum_col("pass_yds", "pass_yards")
    sum_col("pass_td", "pass_tds")
    sum_col("int", "interceptions")

    # RBs: rush_att, rush_yds, rush_td, tgt, rec_yds, rec_td
    sum_col("rush_att", "rush_attempts")
    sum_col("rush_yds", "rush_yards")
    sum_col("rush_td", "rush_tds")

    # WR/RB/TE receiving columns:
    sum_col("rec", "receptions")
    sum_col("rec_yds", "rec_yards")
    sum_col("rec_td", "rec_tds")
    sum_col("tgt", "targets")

    return stats


def get_player_details(api_id: str):
    """
    Combine TheSportsDB profile with Pro-Football-Reference *career* stats.
    """
    key = current_app.config.get("THESPORTSDB_API_KEY")
    base = current_app.config.get("THESPORTSDB_BASE_URL")
    url = f"{base}/{key}/lookupplayer.php"

    try:
        resp = requests.get(url, params={"id": api_id}, timeout=5)
        resp.raise_for_status()
    except requests.RequestException as e:
        current_app.logger.error("TheSportsDB lookup error: %s", e)
        return None

    data = resp.json() or {}
    players = data.get("players") or []
    if not players:
        return None

    p = players[0]

    sport = (p.get("strSport") or "").lower()
    if sport and "football" not in sport:
        return None

    details = {
        "api_id": p.get("idPlayer"),
        "name": p.get("strPlayer"),
        "position": p.get("strPosition"),
        "team": p.get("strTeam"),
        "nationality": p.get("strNationality"),
        "league": p.get("strLeague"),
        "birth_date": p.get("dateBorn"),
        "birth_place": p.get("strBirthLocation"),
        "height": p.get("strHeight"),
        "weight": p.get("strWeight"),
        "college": p.get("strCollege"),
        "number": p.get("strNumber"),
        "thumb": p.get("strThumb"),
        "banner": p.get("strBanner"),
        "description": p.get("strDescriptionEN"),
    }

    # Attach career stats from Pro-Football-Reference
    career = get_pfr_career_stats(details["name"], details["position"])
    if career:
        details["career_stats"] = career

    return details


# --------------------------- Routes ------------------------------------ #

@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/search")
def search():
    query = request.args.get("q", "").strip()
    api_results = []

    if query:
        # Log search (for your DB / core component 2)
        log = SearchLog(
            query=query,
            client_ip=request.remote_addr or "unknown",
        )
        db.session.add(log)
        db.session.commit()

        current_app.logger.info("Search query: %s", query)
        api_results = search_players_api(query)

    return render_template(
        "search.html",
        query=query,
        api_results=api_results,
    )


@main_bp.route("/player/<api_id>")
def player_detail(api_id):
    player = get_player_details(api_id)
    if not player:
        abort(404)
    return render_template("player.html", player=player)
