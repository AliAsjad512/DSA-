import os
import boto3
import json
import argparse
import time
from datetime import datetime

class TerraformStateManager:
     def __init__(self, bucket, key, region='us-east-1'):
        self.bucket = bucket
        self.key = key
        self.s3 = boto3.client('s3', region_name=region)
        self.lock_table = None  # DynamoDB table for locking
     def enable_state_locking(self, table_name):
        """Enable DynamoDB state locking"""
        self.lock_table = boto3.resource('dynamodb').Table(table_name)

     def get_state(self):
        """Download current state file"""
        try:
            response = self.s3.get_object(Bucket=self.bucket, Key=self.key)
            return json.loads(response['Body'].read())
        except self.s3.exceptions.NoSuchKey:
            return None
        except Exception as e:
            print(f"❌ Error reading state: {e}")
            return None