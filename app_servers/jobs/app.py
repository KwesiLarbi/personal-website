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

from jobs import *


@app.route('/')
def home():
    """
    Route that returns the status of each job
    """
    return 'status: <none>'


if __name__ == '__main__':
    app.run()