Ansible Dynamic Inventory Script for AWS EC2
Returns JSON in Ansible inventory format
"""

import argparse
import sys
import json
import boto3
from botocore.exceptions import ClientError

def get_ec2_instances(filters=None):
    """Get EC2 instances with optional filters"""
    ec2 = boto3.client('ec2')
    instances = []
    paginator = ec2.get_paginator('describe_instances')
    for page in paginator.paginate(Filters=filters or []):
        for reservation in page['Reservations']:
            for instance in reservation['Instances']:
                # Only include running instances
                if instance['State']['Name'] == 'running':
                    instances.append(instance)
    return instances

    def build_inventory(instances, group_by='tag:Environment'):
    """Build Ansible inventory from instances"""
    inventory = {
        '_meta': {
            'hostvars': {}
        }
    }