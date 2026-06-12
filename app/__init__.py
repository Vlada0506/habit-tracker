from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    instance_path = Path(app.instance_path)
    instance_path.mkdir(parents=True, exist_ok=True)

    app.config["SECRET_KEY"] = "habit-tracker-secret-key"

    if test_config:
        app.config.update(test_config)
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = (
            f"sqlite:///{instance_path / 'habits.db'}"
        )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from app.models import Habit, Completion
    from app.routes import main

    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app