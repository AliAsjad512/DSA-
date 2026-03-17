CI/CD Pipeline Monitor - Check Jenkins job status and send alerts


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

            def get_last_build_status(self, job_name):
        Get status of last build for a job
        job = self.get_job_info(job_name)
        if not job:
            return None
        
        last_build = job.get('lastBuild')
        if not last_build:
            return {'status': 'NO_BUILDS', 'timestamp': None}
        
        build_number = last_build['number']
        build_url = f"{self.url}/job/{job_name}/{build_number}/api/json"
        try:
            response = self.session.get(build_url)
            response.raise_for_status()
            build = response.json()
            return {
                'status': build['result'],
                'timestamp': datetime.fromtimestamp(build['timestamp']/1000).isoformat(),
                'duration': build.get('duration', 0),
                'url': build['url']
            }
        except Exception as e:
            print(f"❌ Error fetching build {build_number} for {job_name}: {e}")
            return None
        
        def get_last_build_status(self, job_name):
        """Get status of last build for a job"""
        job = self.get_job_info(job_name)
        if not job:
            return None
        
        last_build = job.get('lastBuild')
        if not last_build:
            return {'status': 'NO_BUILDS', 'timestamp': None}
        
        build_number = last_build['number']
        build_url = f"{self.url}/job/{job_name}/{build_number}/api/json"
        try:
            response = self.session.get(build_url)
            response.raise_for_status()
            build = response.json()
            return {
                'status': build['result'],
                'timestamp': datetime.fromtimestamp(build['timestamp']/1000).isoformat(),
                'duration': build.get('duration', 0),
                'url': build['url']
            }
        except Exception as e:
            print(f"❌ Error fetching build {build_number} for {job_name}: {e}")
            return None
        
          def monitor_jobs(self, job_list):
        
        results = {}
        for job in job_list:
            print(f"🔍 Checking job: {job}")
            status = self.get_last_build_status(job)
            results[job] = status
        return results
    
    def send_email_alert(self, failed_jobs, smtp_config):
        """Send email alert for failed jobs"""
        msg = MIMEMultipart()
        msg['From'] = smtp_config['from']
        msg['To'] = smtp_config['to']
        msg['Subject'] = f"Jenkins Alert: {len(failed_jobs)} job(s) failed"

        body = "The following Jenkins jobs have failed:\n\n"
        for job, info in failed_jobs.items():
            body += f"- {job}: {info['url']} (at {info['timestamp']})\n"

        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP(smtp_config['host'], smtp_config['port'])
            if smtp_config.get('tls'):
                server.starttls()
            if smtp_config.get('user'):
                server.login(smtp_config['user'], smtp_config['password'])
            server.send_message(msg)
            server.quit()
            print("✅ Alert email sent")
        except Exception as e:
            print(f"❌ Failed to send email: {e}")