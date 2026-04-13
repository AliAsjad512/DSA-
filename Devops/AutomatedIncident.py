import subprocess
import argparse
import json
import time
import requests
import logging
from pathlib import Path

class IncidentResponder:
    def __init__(self, runbook_dir='./runbooks'):
        self.runbook_dir = Path(runbook_dir)
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    def load_runbook(self, incident_type):
        """Load runbook configuration from JSON"""
        runbook_file = self.runbook_dir / f"{incident_type}.json"
        if not runbook_file.exists():
            raise FileNotFoundError(f"Runbook {incident_type} not found")
        with open(runbook_file) as f:
            return json.load(f)
    def execute_step(self, step):
        """Execute a single runbook step"""
        step_type = step.get('type')
        self.logger.info(f"Executing step: {step.get('name', 'unnamed')}")

        if step_type == 'command':
            result = subprocess.run(step['command'], shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                raise Exception(f"Command failed: {result.stderr}")
            return result.stdout
        elif step_type == 'http':
            method = step.get('method', 'GET').upper()
            url = step['url']
            headers = step.get('headers', {})
            data = step.get('data')
            if method == 'GET':
                resp = requests.get(url, headers=headers, timeout=10)
            elif method == 'POST':
                resp = requests.post(url, headers=headers, json=data, timeout=10)
            else:
                raise ValueError(f"Unsupported HTTP method {method}")
            resp.raise_for_status()
            return resp.json()
        elif step_type == 'sleep':
            time.sleep(step.get('duration', 5))
            return "Slept"
        elif step_type == 'webhook':
            # Slack/Teams notification
            webhook_url = step['webhook_url']
            message = step.get('message', 'Incident response step executed')
            requests.post(webhook_url, json={'text': message}, timeout=5)
            return "Notification sent"
        else:
            raise ValueError(f"Unknown step type: {step_type}")
