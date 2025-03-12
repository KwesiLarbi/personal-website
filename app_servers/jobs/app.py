import os

from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from rq import Queue
from rq.job import Job
from worker import conn

app = Flask(__name__)

# load environmental variables
load_dotenv()

env_config = os.getenv('APP_SETTINGS', 'config.DevelopmentConfig')
app.config.from_object(env_config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# set up redis connection and initializing queue
q = Queue(connection=conn)

@app.route('/')
def index():
    from jobs import init_get_github_repos

    job = q.enqueue_call(
        func=init_get_github_repos, result_ttl=5000
    )
    print(job.get_id)

    return 'hello world'

# @app.route('/results/<job_key>', methods = ['GET'])
# def get_results(job_key):
#     job = Job.fetch(job_key, connection=conn)

#     if job.is_finished:
#         return str(job.result), 200
#     else:
#         return 'Nay!', 202

if __name__ == '__main__':
    app.run()