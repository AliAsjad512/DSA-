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