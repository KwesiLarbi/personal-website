import redis

from rq import Queue, Connection
from flask import Blueprint, jsonify, current_app

from .jobs import init_get_github_repos

bp = Blueprint('main', __name__)

@bp.route('/jobs', methods = ["POST"])
def run_init_git_task():
    with Connection(redis.from_url(current_app.config['REDIS_URL'])):
        q = Queue()
        job = q.enqueue(init_get_github_repos)

    response_obj = {
        'status': 'success',
        'data': {
            'task_id': job.get_id()
        }
    }

    return jsonify(response_obj), 202

@bp.route('/jobs/<job_id>', methods = ['GET'])
def get_job_status(job_id):
    with Connection(redis.from_url(current_app.config['REDIS_URL'])):
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