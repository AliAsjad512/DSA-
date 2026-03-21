"""
Disk Usage Monitor - Check disk usage and send alerts via email/Slack
"""

import psutil
import argparse
import smtplib
import requests
from email.mime.text import MIMEText
import json
import time
import os

class DiskMonitor:
    def __init__(self, threshold=80, path='/'):
        self.threshold = threshold
        self.path = path
        self.alert_sent = False  # To avoid repeated alerts
        def check_disk_usage(self):
        """Get disk usage percentage for given path"""
        usage = psutil.disk_usage(self.path)
        percent = usage.percent
        free_gb = usage.free / (1024**3)
        total_gb = usage.total / (1024**3)
        return {
            'percent': percent,
            'free_gb': round(free_gb, 2),
            'total_gb': round(total_gb, 2),
            'used_gb': round(usage.used / (1024**3), 2),
            'path': self.path
        }

    def send_email_alert(self, info, smtp_config):
        """Send email alert"""
        msg = MIMEText(f"""
Disk Usage Alert!
                       Path: {info['path']}
Current usage: {info['percent']}%
Free space: {info['free_gb']} GB
Total: {info['total_gb']} GB

Threshold: {self.threshold}%
""")
        msg['Subject'] = f"⚠️ Disk Usage Alert: {info['percent']}% on {info['path']}"
        msg['From'] = smtp_config['from']
        msg['To'] = smtp_config['to']

        try:
            server = smtplib.SMTP(smtp_config['host'], smtp_config['port'])
            if smtp_config.get('tls'):
                server.starttls()
            if smtp_config.get('user'):
                server.login(smtp_config['user'], smtp_config['password'])
            server.send_message(msg)
            server.quit()
            print("✅ Email alert sent")
        except Exception as e:
            print(f"❌ Failed to send email: {e}")g