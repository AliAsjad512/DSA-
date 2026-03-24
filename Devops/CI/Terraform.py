#!/usr/bin/env python3
#Terraform State Manager - Backup, lock, and manage Terraform state files


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
   def put_state(self, state):
        """Upload state file with locking"""
        if self.lock_table:
            # Attempt to acquire lock
            if not self._acquire_lock():
                raise Exception("Failed to acquire lock, another process is using state")
        try:
            self.s3.put_object(
                Bucket=self.bucket,
                Key=self.key,
                Body=json.dumps(state, indent=2),
                ContentType='application/json'
            )
            print("✅ State saved successfully")
        finally:
            if self.lock_table:
                self._release_lock()

