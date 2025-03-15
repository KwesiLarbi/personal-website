import datetime

# from app import db
from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Repos(db.Model):
    __tablename__ = 'repos'

    id = db.Column(db.Integer, primary_key = True)
    job_id = db.Column(db.Uuid)
    full_name = db.Column(db.String())
    description = db.Column(db.String())
    forks_count = db.Column(db.Integer)
    stargazers_count = db.Column(db.Integer)
    watchers_count = db.Column(db.Integer)
    size = db.Column(db.Integer)
    language = db.Column(db.String())
    pushed_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)