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
    def compute_metrics(self, runs):
        """Compute success rate, average duration, etc."""
        total = len(runs)
        if total == 0:
            return {}
        successes = sum(1 for r in runs if r['conclusion'] == 'success')
        failures = sum(1 for r in runs if r['conclusion'] == 'failure')
        avg_duration = sum(r['duration'] for r in runs) / total
        return {
            'total_runs': total,
            'success_rate': round(successes / total * 100, 2),
            'failure_count': failures,
            'avg_duration_seconds': round(avg_duration, 2),
            'trend': self._calculate_trend(runs)
        }
    def _calculate_trend(self, runs, window=7):
        """Calculate trend over last N runs"""
        recent = runs[:window]
        older = runs[window:window*2] if len(runs) >= window*2 else runs[:window//2]
        if not older or not recent:
            return 'insufficient_data'
        recent_success = sum(1 for r in recent if r['conclusion'] == 'success') / len(recent)
        older_success = sum(1 for r in older if r['conclusion'] == 'success') / len(older)
        if recent_success > older_success + 0.1:
            return 'improving'
        elif recent_success < older_success - 0.1:
            return 'declining'
        return 'stable'
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='GitHub Actions Metrics')
    parser.add_argument('--repo', required=True, help='Owner/repo')
    parser.add_argument('--token', required=True, help='GitHub token')
    parser.add_argument('--workflow', help='Workflow filename or ID')
    parser.add_argument('--days', type=int, default=30)
    args = parser.parse_args()

    metrics = GHAMetrics(args.repo, args.token)
    runs = metrics.get_workflow_runs(args.workflow, args.days)
    stats = metrics.compute_metrics(runs)
    print(f"📊 GitHub Actions Metrics for {args.repo}")
    print(f"  Total runs (last {args.days} days): {stats.get('total_runs', 0)}")
    print(f"  Success rate: {stats.get('success_rate', 0)}%")
    print(f"  Avg duration: {stats.get('avg_duration_seconds', 0)} seconds")
    print(f"  Trend: {stats.get('trend', 'unknown')}")