import os
import redis

from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_migrate import Migrate
from rq import Queue, Connection
from rq.job import Job
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

    @app.route('/')
    def index():
        from .jobs import init_get_github_repos

        with Connection(redis.from_url(app.config['REDIS_URL'])):
            q = Queue()
            job = q.enqueue_call(
                func=init_get_github_repos, result_ttl=5000
            )

        response_obj = {
            'status': 'success',
            'data': {
                'task_id': job.get_id()
            }
        }

        return jsonify(response_obj), 202
    
    @app.route('/jobs/<job_id>', methods = ['GET'])
    def get_job_status(job_id):
        with Connection(redis.from_url(app.config['REDIS_URL'])):
            q = Queue()
            job = q.fetch_job(job_id)
        
        if job:
            response_obj = {
                'status': 'success',
                'data': {
                    'job_id': job.get_id(),
                    'job_status': job.get_status(),
                    'job_result': job.result,
                },
            }
        else:
            response_obj = {'status': 'error'}

        return jsonify(response_obj)

    return app