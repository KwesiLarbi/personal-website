import os
import json

from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_migrate import Migrate
from atproto import Client

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

    from .models import Repos, Posts

    with app.app_context():
        db.create_all()

    from . import views
    app.register_blueprint(views.bp)

    @app.route('/test-bsky', methods = ['GET'])
    def test_bsky_get_user_feed():
        bsky_handle = os.getenv('BSKY_HANDLE')
        bsky_pw = os.getenv('BSKY_PASSWORD')
        client = Client()
        client.login(bsky_handle, bsky_pw)
        profile = client.get_profile(actor=bsky_handle)
        did = profile.did
        data = client.get_author_feed(
            actor=did,
            filter='posts_and_author_threads',
            limit=5,
        )
        feed = data.model_dump_json()

        return feed

    return app