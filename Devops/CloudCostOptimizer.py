import boto3
import datetime
import json
import argparse
import numpy as np
from collections import defaultdict

class CostAnomalyDetector:
    def __init__(self, region='us-east-1'):
        self.ce = boto3.client('ce', region_name=region)

    def get_daily_costs(self, days_back=30):
        """Retrieve daily costs for last N days"""
        end = datetime.date.today()
        start = end - datetime.timedelta(days=days_back)
        response = self.ce.get_cost_and_usage(
            TimePeriod={
                'Start': start.strftime('%Y-%m-%d'),
                'End': end.strftime('%Y-%m-%d')
            },
            Granularity='DAILY',
            Metrics=['UnblendedCost'],
            GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
        )
        daily_data = defaultdict(dict)
        for result in response['ResultsByTime']:
            date = result['TimePeriod']['Start']
            for group in result['Groups']:
                service = group['Keys'][0]
                cost = float(group['Metrics']['UnblendedCost']['Amount'])
                daily_data[date][service] = cost
        return daily_data