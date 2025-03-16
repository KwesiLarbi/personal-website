import os
import requests
import json
import uuid

from requests.auth import HTTPBasicAuth
from sqlalchemy import exc
# from atproto import Client

from .models import Repos
from . import db

#########################################
############# GITHUB JOBS ###############
#########################################

token = os.getenv('GH_TOKEN')
bsky_handle = os.getenv('BSKY_HANDLE')
bsky_pw = os.getenv('BSKY_PASSWORD')
url = 'https://api.github.com/user/repos'

def init_get_github_repos():
    errors = []
    job_id = uuid.uuid4()

    try:
        results = requests.get(url, auth=HTTPBasicAuth('user', token))
        results.raise_for_status()
    except requests.exceptions.HTTPError as e:
        errors.append(f'Unable to get URL. Please try again: \n{e}')
        return {"errors": errors}

    output = json.loads(results.text)

    # save results
    try:
        # repos = Repos(repos_arr)
        for i in output:
            repos = Repos(
                id=i['id'],
                job_id=job_id,
                full_name=i['full_name'],
                description=str(i['description']),
                forks_count=i['forks_count'],
                stargazers_count=i['stargazers_count'],
                watchers_count=i['watchers_count'],
                size=i['size'],
                language=i['language'],
                pushed_at=i['pushed_at'],
                created_at=i['created_at'],
                updated_at=i['updated_at']
            )
            db.session.add(repos)
            db.session.commit()
            
        return repos.job_id
    except exc.SQLAlchemyError as e:
        errors.append(f'Could not save results of current job: \n{e}')
        return {"errors": errors}
    

#########################################
############# BSKY JOBS #################
#########################################

# def test_bsky_create_post():
    #     bsky_handle = os.getenv('BSKY_HANDLE')
    #     bsky_pw = os.getenv('BSKY_PASSWORD')
    #     client = Client()
    #     client.login(bsky_handle, bsky_pw)
    #     post = client.send_post('Hello world! I posted this via the Python SDK.')

    #     return post.uri

    # test_bsky_create_post()