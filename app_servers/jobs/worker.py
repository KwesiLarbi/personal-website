import os

import redis
from flask.cli import FlaskGroup
from rq import Worker, Queue, Connection

from server import create_app

app = create_app()
cli = FlaskGroup(create_app=create_app)

# listen = ['default']

# redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis_url = app.config['REDIS_URL']

conn = redis.from_url(redis_url)

@cli.command('run_worker')
def run_worker():
    with Connection(conn):
        worker = Worker(list(map(Queue, app.config['QUEUES'])))
        worker.work()

if __name__ == '__main__':
    cli()