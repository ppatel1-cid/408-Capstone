from datetime import datetime
from . import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(128), nullable=False, index=True)
    position = db.Column(db.String(10), nullable=False)
    team = db.Column(db.String(64), nullable=True)
    seasons = db.Column(db.Integer, nullable=False)
    games_played = db.Column(db.Integer, nullable=False)
    total_yards = db.Column(db.Integer, nullable=False)
    touchdowns = db.Column(db.Integer, nullable=False)
    interceptions = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class SearchLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String(128), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    client_ip = db.Column(db.String(45))

from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
