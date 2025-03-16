import datetime
import uuid

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

class Posts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Uuid, primary_key = True, default=uuid.uuid4()) # general db id, uuid auto-generated
    post_id = db.Column(db.String(), default=None) # id comes from social media source
    username = db.Column(db.String())
    user_id = db.Column(db.String())
    avi = db.Column(db.String())
    text = db.Column(db.String())
    uri = db.Column(db.String()) # posts location
    like_count = db.Column(db.Integer)
    quote_count = db.Column(db.Integer)
    reply_count = db.Column(db.Integer)
    repost_count = db.Column(db.Integer)
    source = db.Column(db.String()) # social media source
    created_at = db.Column(db.DateTime)
