import requests
import argparse
import json
import datetime
from collections import defaultdict

class GHAMetrics:
    def __init__(self, repo, token):
        self.repo = repo
        self.headers = {'Authorization': f'token {token}', 'Accept': 'application/vnd.github.v3+json'}
        self.base_url = f'https://api.github.com/repos/{repo}'
    def get_workflow_runs(self, workflow_id=None, days_back=30):
        """Fetch workflow runs from GitHub API"""
        url = f'{self.base_url}/actions/runs'
        if workflow_id:
            url += f'?workflow_id={workflow_id}'
        params = {'per_page': 100, 'status': 'completed'}
        runs = []
        page = 1
        while True:
            resp = requests.get(url, headers=self.headers, params={**params, 'page': page})
            if resp.status_code != 200:
                break
            data = resp.json()
            if not data.get('workflow_runs'):
                break
            for run in data['workflow_runs']:
                created_at = datetime.datetime.fromisoformat(run['created_at'].replace('Z', '+00:00'))
                cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=days_back)
                if created_at < cutoff:
                    break
                runs.append({
                    'id': run['id'],
                    'name': run['name'],
                    'conclusion': run['conclusion'],
                    'created_at': run['created_at'],
                    'duration': (datetime.datetime.fromisoformat(run['updated_at'].replace('Z', '+00:00')) -
                                 datetime.datetime.fromisoformat(run['created_at'].replace('Z', '+00:00'))).total_seconds()
                })
            if len(data['workflow_runs']) < 100:
                break
            page += 1
        return runs