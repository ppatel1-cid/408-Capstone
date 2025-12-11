import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "mysupersecretkey123")

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" + os.path.join(os.getcwd(), "instance", "nfl_stats.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # TheSportsDB NFL API (for basic profile + photos)
    THESPORTSDB_API_KEY = os.environ.get("THESPORTSDB_API_KEY", "3")
    THESPORTSDB_BASE_URL = "https://www.thesportsdb.com/api/v1/json"

    # Pro Football Reference: which season to summarize from game logs
    # (You can change this to 2024 later if you want.)
    PFR_DEFAULT_SEASON = int(os.environ.get("PFR_DEFAULT_SEASON", "2023"))
