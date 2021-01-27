from . import api
import os


@api.route('/repos/transfer', methods=['POST'])
def get_user():
    token = os.getenv('GITHUB_TOKEN')

    owner = sys.argv[1]
    repo = sys.argv[2]
    new_owner = sys.argv[3]

    query_url = f"https://api.github.com/repos/{owner}/{repo}/transfer"

    headers = {'Authorization': f'token {token}',
               'Accept': 'application/vnd.github.v3+json'}
    params = {
        'new_owner': new_owner,
    }

    r = requests.post(query_url, headers=headers, data=json.dumps(params))

    pprint(r.status_code)
    pprint(r.json())
