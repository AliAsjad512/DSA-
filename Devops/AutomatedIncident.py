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