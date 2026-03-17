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