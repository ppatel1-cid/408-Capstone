import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    # ----------------------------------------
    # Create Flask app
    # ----------------------------------------
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("app.config.Config")

    # ----------------------------------------
    # Ensure instance folder exists
    # ----------------------------------------
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    # ----------------------------------------
    # Init DB
    # ----------------------------------------
    db.init_app(app)

    # ----------------------------------------
    # Logging setup
    # ----------------------------------------
    log_dir = os.path.join(app.root_path, "..", "logs")
    os.makedirs(log_dir, exist_ok=True)

    file_handler = RotatingFileHandler(
        os.path.join(log_dir, "app.log"), maxBytes=10240, backupCount=5
    )
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s"
    )
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)

    # ----------------------------------------
    # Import & Register Blueprints HERE
    # ----------------------------------------
    from app.routes import main_bp
    from app.auth import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    # ----------------------------------------
    # Return app object
    # ----------------------------------------
    return app
