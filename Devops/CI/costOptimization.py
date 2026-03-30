import boto3
import os
import argparse
import datetime
import gzip
import shutil
import hashlib
import logging
from pathlib import Path

class AWSCostOptimizer:
    def __init__(self, region='us-east-1'):
        self.region = region
        self.ec2 = boto3.client('ec2', region_name=region)
        self.elb = boto3.client('elbv2', region_name=region)
        self.rds = boto3.client('rds', region_name=region)
        self.cw = boto3.client('cloudwatch', region_name=region)

        def find_idle_ec2_instances(self, days=30):
        """Find EC2 instances with low CPU usage over last N days"""
        instances = self.ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        idle = []
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                # Get CPU utilization metrics
                end = datetime.datetime.utcnow()
                start = end - datetime.timedelta(days=days)
                response = self.cw.get_metric_statistics(
                    Namespace='AWS/EC2',
                    MetricName='CPUUtilization',
                    Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                    StartTime=start,
                    EndTime=end,
                    Period=86400,  # daily
                    Statistics=['Average']
                )
                if response['Datapoints']:
                    avg_cpu = sum(dp['Average'] for dp in response['Datapoints']) / len(response['Datapoints'])
                    if avg_cpu < 5:  # threshold
                        idle.append({
                            'InstanceId': instance_id,
                            'InstanceType': instance['InstanceType'],
                            'AverageCPU': round(avg_cpu, 2),
                            'Name': [tag['Value'] for tag in instance.get('Tags', []) if tag['Key'] == 'Name']
                        })
        return idle
    
     def find_unused_elbs(self):
        """Find load balancers with no traffic"""
        elbs = self.elb.describe_load_balancers()['LoadBalancers']
        unused = []
        for lb in elbs:
            arn = lb['LoadBalancerArn']
            # Check request count
            end = datetime.datetime.utcnow()
            start = end - datetime.timedelta(days=7)
            try:
                response = self.cw.get_metric_statistics(
                    Namespace='AWS/ApplicationELB',
                    MetricName='RequestCount',
                    Dimensions=[{'Name': 'LoadBalancer', 'Value': arn.split('/')[-1]}],
                    StartTime=start,
                    EndTime=end,
                    Period=3600,
                    Statistics=['Sum']
                )
                total_requests = sum(dp['Sum'] for dp in response['Datapoints']) if response['Datapoints'] else 0
                if total_requests == 0:
                    unused.append({
                        'LoadBalancerName': lb['LoadBalancerName'],
                        'DNSName': lb['DNSName'],
                        'State': lb['State']['Code']
                    })
            except:
                pass
        return unused
        
