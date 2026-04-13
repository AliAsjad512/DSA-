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
