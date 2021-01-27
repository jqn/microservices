from . import api
import os
from flask import request

token = os.getenv('GITHUB_TOKEN')


@api.route('/repos/transfer', methods=['POST'])
def get_user():

    owner = request.args.get("owner", "jqn")
    repo = request.args.get("repo", "")
    new_owner = request.args.get("new_owner", "")

    query_url = f"https://api.github.com/repos/{owner}/{repo}/transfer"

    headers = {'Authorization': f'token {token}',
               'Accept': 'application/vnd.github.v3+json'}
    params = {
        'new_owner': new_owner,
    }

    r = requests.post(query_url, headers=headers, data=json.dumps(params))

    pprint(r.status_code)
    pprint(r.json())
