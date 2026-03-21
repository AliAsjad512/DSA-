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