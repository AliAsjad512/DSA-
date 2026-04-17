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