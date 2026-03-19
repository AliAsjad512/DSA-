Ansible Dynamic Inventory Script for AWS EC2
Returns JSON in Ansible inventory format
"""

import argparse
import sys
import json
import boto3
from botocore.exceptions import ClientError