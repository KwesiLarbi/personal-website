import os
import requests
import json

from requests.auth import HTTPBasicAuth

token = os.getenv('GH_TOKEN')
url = 'https://api.github.com/user/repos'
output = requests.get(url, auth=HTTPBasicAuth('user', token))
output = json.loads(output.text)
repos = []

for i in output:
    results = {
        'id': i['id'],
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
    repos.append(results)

print(repos)