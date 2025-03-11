import os
import requests
import json
import uuid

from requests.auth import HTTPBasicAuth
from sqlalchemy import exc

from models import *
from app import db

token = os.getenv('GH_TOKEN')
url = 'https://api.github.com/user/repos'

def init_get_github_repos():
    repos_arr = []
    errors = []
    job_id = uuid.uuid4()

    try:
        results = requests.get(url, auth=HTTPBasicAuth('user', token))
        results.raise_for_status()
    except requests.exceptions.HTTPError as e:
        errors.append(f'Unable to get URL. Please try again: \n{e}')
        return {"errors": errors}

    output = json.loads(results.text)

    for i in output:
        repo = {
            'id': i['id'],
            'job_id': job_id,
            'full_name': i['full_name'],
            'description': str(i['description']),
            'forks_count': i['forks_count'],
            'stargazers_count': i['stargazers_count'],
            'watchers_count': i['watchers_count'],
            'size': i['size'],
            'language': i['language'],
            'pushed_at': i['pushed_at'],
            'created_at': i['created_at'],
            'updated_at': i['updated_at']
        }
        repos_arr.append(repo)

    # save results
    try:
        repos = Repos(repos_arr)
        db.session.add(repos)
        db.session.commit()
        print(repos.job_id)
        # return repos.job_id
    except exc.SQLAlchemyError as e:
        pass