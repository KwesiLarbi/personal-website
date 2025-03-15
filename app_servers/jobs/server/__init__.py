import os
import redis

from flask import Flask, jsonify
from dotenv import load_dotenv
# from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from rq import Queue, Connection
from rq.job import Job
from .models import db

load_dotenv()

migrate = Migrate()

# set up redis connection and initializing queue
# q = Queue(connection=conn)

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

        # print(job.get_id)

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


# # load environmental variables
# load_dotenv()

# app = Flask(__name__)
# env_config = os.getenv('APP_SETTINGS', 'config.DevelopmentConfig')
# app.config.from_object(env_config)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# # set up redis connection and initializing queue
# q = Queue(connection=conn)

# from models import *

# @app.route('/')
# def index():
#     from jobs import init_get_github_repos

#     job = q.enqueue_call(
#         func=init_get_github_repos, result_ttl=5000
#     )
#     print(job.get_id)

#     return 'hello world'

# @app.route('/results/<job_key>', methods = ['GET'])
# def get_results(job_key):
#     job = Job.fetch(job_key, connection=conn)

#     if job.is_finished:
#         return str(job.result), 200
#     else:
#         return 'Nay!', 202


# if __name__ == '__main__':
#     app.run()