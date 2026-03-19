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

    for instance in instances:
        hostname = instance.get('PublicDnsName') or instance.get('PrivateDnsName') or instance['InstanceId']
        host_vars = {
            'ansible_host': instance.get('PublicIpAddress') or instance.get('PrivateIpAddress'),
            'ec2_id': instance['InstanceId'],
            'ec2_instance_type': instance['InstanceType'],
            'ec2_private_ip': instance.get('PrivateIpAddress'),
            'ec2_public_ip': instance.get('PublicIpAddress'),
            'ec2_region': instance['Placement']['AvailabilityZone'][:-1],
            'ec2_az': instance['Placement']['AvailabilityZone'],
            'ec2_tags': {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
        }
        inventory['_meta']['hostvars'][hostname] = host_vars

        # Determine groups
        groups = ['all']
        # Add tag-based groups
        tags = host_vars['ec2_tags']
        for key, value in tags.items():
            groups.append(f"tag_{key}_{value}")
            groups.append(f"tag_{key}")
        # Add instance type group
        groups.append(f"type_{instance['InstanceType']}")
        # Add security group groups
        for sg in instance.get('SecurityGroups', []):
            groups.append(f"sg_{sg['GroupName']}")

        # Add host to each group
        for group in set(groups):  # remove duplicates
            if group not in inventory:
                inventory[group] = {'hosts': []}
            if hostname not in inventory[group]['hosts']:
                inventory[group]['hosts'].append(hostname)

    return inventory