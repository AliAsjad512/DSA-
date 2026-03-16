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

         def get_ec2_instances(self):
        """Get all EC2 instances"""
        instances = []
        paginator = self.ec2.get_paginator('describe_instances')
        for page in paginator.paginate():
            for reservation in page['Reservations']:
                for instance in reservation['Instances']:
                    instances.append({
                        'InstanceId': instance['InstanceId'],
                        'InstanceType': instance['InstanceType'],
                        'State': instance['State']['Name'],
                        'LaunchTime': instance['LaunchTime'].isoformat(),
                        'PublicIp': instance.get('PublicIpAddress', 'N/A'),
                        'PrivateIp': instance.get('PrivateIpAddress', 'N/A'),
                        'Tags': {t['Key']: t['Value'] for t in instance.get('Tags', [])}
                    })
        return instances
