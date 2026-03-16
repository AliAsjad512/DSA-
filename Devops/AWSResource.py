AWS Resource Inventory - List all EC2 instances, S3 buckets, and RDS instances
"""

import boto3
import json
from datetime import datetime
import argparse

class AWSInventory:
    def __init__(self, region='us-east-1'):
        self.region = region
        self.ec2 = boto3.client('ec2', region_name=region)
        self.s3 = boto3.client('s3')
        self.rds = boto3.client('rds', region_name=region)
        self.resources = {}
