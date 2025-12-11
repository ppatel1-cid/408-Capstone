import requests
from flask import current_app

def search_players_api(name: str):
    """
    Search TheSportsDB for NFL players that match the given name.
    Returns a list of simple dicts for the template.
    """
    key = current_app.config["THESPORTSDB_API_KEY"]
    base = current_app.config["THESPORTSDB_BASE_URL"]
    url = f"{base}/{key}/searchplayers.php"

    try:
        resp = requests.get(url, params={"p": name}, timeout=5)
        resp.raise_for_status()
    except requests.RequestException as e:
        current_app.logger.error("TheSportsDB API error: %s", e)
        return []

    data = resp.json() or {}
    players = data.get("player") or []

    # Filter to NFL / American Football only
    nfl_players = [
        p for p in players
        if p.get("strSport") == "American Football"
           and ("NFL" in (p.get("strLeague") or ""))
    ]

    results = []
    for p in nfl_players:
        results.append({
            "api_id": p.get("idPlayer"),
            "name": p.get("strPlayer"),
            "position": p.get("strPosition"),
            "team": p.get("strTeam"),
            "nationality": p.get("strNationality"),
            "thumb": p.get("strThumb"),
        })
    return results
