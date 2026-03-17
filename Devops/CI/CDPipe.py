CI/CD Pipeline Monitor - Check Jenkins job status and send alerts
"""

import requests
from requests.auth import HTTPBasicAuth
import json
import argparse
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class JenkinsMonitor:
    def __init__(self, url, username, password):
        self.url = url.rstrip('/')
        self.auth = HTTPBasicAuth(username, password)
        self.session = requests.Session()
        self.session.auth = self.auth

    def get_job_info(self, job_name):
        """Get detailed information about a Jenkins job"""
        api_url = f"{self.url}/job/{job_name}/api/json"
        try:
            response = self.session.get(api_url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"❌ Error fetching job {job_name}: {e}")
            return None