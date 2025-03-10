import requests
import json
import os

from flask import Flask
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

"""
Eventual function/process. Will check if database is empty,
if empty, make a call to GitHub and for repo data and load into
postgres database table
""" 
token = os.getenv('GH_TOKEN')
url = 'https://api.github.com/user/repos'
output = requests.get(url, auth=HTTPBasicAuth('user', token))
output = json.loads(output.text)
repos = []

for i in output:
    results = {
        'id': i['id'],
        'full_name': i['full_name'],
        'description': i['description'],
        'forks_count': i['forks_count'],
        'stargazers_count': i['stargazers_count'],
        'watchers_count': i['watchers_count'],
        'size': i['size'],
        'language': i['language'],
        'pushed_at': i['pushed_at'],
        'created_at': i['created_at'],
        'updated_at': i['updated_at']
    }
    repos.append(results)

print(repos)

# Routes #
@app.route('/')
def home():
    return 'status: <none>'