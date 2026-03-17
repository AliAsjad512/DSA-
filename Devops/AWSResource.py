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

        def get_s3_buckets(self):
        """Get all S3 buckets"""
        buckets = []
        response = self.s3.list_buckets()
        for bucket in response['Buckets']:
            buckets.append({
                'Name': bucket['Name'],
                'CreationDate': bucket['CreationDate'].isoformat()
            })
        return buckets


        
    def get_rds_instances(self):
        """Get all RDS instances"""
        instances = []
        paginator = self.rds.get_paginator('describe_db_instances')
        for page in paginator.paginate():
            for db in page['DBInstances']:
                instances.append({
                    'DBInstanceIdentifier': db['DBInstanceIdentifier'],
                    'Engine': db['Engine'],
                    'DBInstanceClass': db['DBInstanceClass'],
                    'Status': db['DBInstanceStatus'],
                    'Endpoint': db['Endpoint']['Address'] if 'Endpoint' in db else 'N/A',
                    'CreatedTime': db['InstanceCreateTime'].isoformat() if 'InstanceCreateTime' in db else 'N/A'
                })
        return instances

        def generate_inventory(self):
        """Generate full inventory"""
        self.resources = {
            'ec2_instances': self.get_ec2_instances(),
            's3_buckets': self.get_s3_buckets(),
            'rds_instances': self.get_rds_instances(),
            'generated_at': datetime.now().isoformat(),
            'region': self.region
        }
        return self.resources
        
    def save_to_file(self, filename=None):
        """Save inventory to JSON file"""
        if not filename:
            filename = f"aws_inventory_{self.region}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(self.resources, f, indent=2, default=str)
        print(f"✅ Inventory saved to {filename}")

        if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AWS Resource Inventory')
    parser.add_argument('--region', default='us-east-1', help='AWS region')
    parser.add_argument('--output', help='Output file name')
    args = parser.parse_args()

    inventory = AWSInventory(region=args.region)
    inventory.generate_inventory()
    inventory.save_to_file(args.output)

    # Print summary
    print(f"\n📊 AWS Inventory Summary ({args.region}):")
    print(f"  EC2 Instances: {len(inventory.resources['ec2_instances'])}")
    print(f"  S3 Buckets: {len(inventory.resources['s3_buckets'])}")
    print(f"  RDS Instances: {len(inventory.resources['rds_instances'])}")