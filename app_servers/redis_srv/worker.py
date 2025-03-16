import os

import redis
from flask.cli import FlaskGroup
from rq import Worker, Connection

from server import create_app

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command('run_worker')
def run_worker():
    redis_url = app.config['REDIS_URL']
    conn = redis.from_url(redis_url)
    with Connection(conn):
        worker = Worker(app.config['QUEUES'])
        worker.work()

if __name__ == '__main__':
    cli()