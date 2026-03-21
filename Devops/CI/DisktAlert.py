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