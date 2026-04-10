import subprocess
import time
import argparse
import logging
import sys
from datetime import datetime
import requests
import socket


class ServiceHealthMonitor:
    def __init__(self, service_name, check_interval=30, max_failures=3):
        self.service_name = service_name
        self.check_interval = check_interval
        self.max_failures = max_failures
        self.failure_count = 0
        self.setup_logging()
def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(f'/var/log/{self.service_name}_monitor.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(self.service_name)


        def check_process(self, process_name=None):
        """Check if process is running"""
        name = process_name or self.service_name
        try:
            result = subprocess.run(['pgrep', '-f', name], capture_output=True, text=True)
            if result.returncode == 0:
                return True, result.stdout.strip()
            return False, None
        except Exception as e:
            return False, str(e)