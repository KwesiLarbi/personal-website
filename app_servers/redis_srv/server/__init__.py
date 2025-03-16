import os

from flask import Flask
from dotenv import load_dotenv
from flask_migrate import Migrate

from .models import db

load_dotenv()

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    env_config = os.getenv('APP_SETTINGS', 'config.DevelopmentConfig')
    app.config.from_object(env_config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    migrate.init_app(app, db)

    from .models import Repos

    with app.app_context():
        db.create_all()

    from . import views
    app.register_blueprint(views.bp)

    return app