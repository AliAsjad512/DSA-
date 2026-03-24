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

                 def _acquire_lock(self):
        """Acquire DynamoDB lock for state file"""
        try:
            self.lock_table.put_item(
                Item={
                    'LockID': self.key,
                    'AcquiredAt': datetime.utcnow().isoformat(),
                    'ExpiresAt': (datetime.utcnow() + timedelta(minutes=15)).isoformat()
                },
                ConditionExpression='attribute_not_exists(LockID)'
            )
            return True
        except:
            return False

    def _release_lock(self):
        """Release DynamoDB lock"""
        self.lock_table.delete_item(Key={'LockID': self.key})

    def backup_state(self, backup_bucket=None):
        """Create a backup of state file"""
        state = self.get_state()
        if not state:
            print("No state file found")
            return
        backup_key = f"{self.key}.{datetime.now().strftime('%Y%m%d_%H%M%S')}.backup"
        if backup_bucket:
            target_bucket = backup_bucket
        else:
            target_bucket = self.bucket
        self.s3.put_object(
            Bucket=target_bucket,
            Key=backup_key,
            Body=json.dumps(state, indent=2)
        )
        print(f"✅ State backed up to s3://{target_bucket}/{backup_key}")
        def diff_state(self, other_state_file):
        """Compare current state with another state file"""
        current = self.get_state()
        with open(other_state_file, 'r') as f:
            other = json.load(f)
        # Simple diff (you could use deepdiff library)
        if current == other:
            print("States are identical")
        else:
            print("States differ")
            # Add detailed diff logic here


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Terraform State Manager')
    parser.add_argument('--bucket', required=True, help='S3 bucket')
    parser.add_argument('--key', required=True, help='State file key')
    parser.add_argument('--action', choices=['get', 'put', 'backup'], required=True)
    parser.add_argument('--state-file', help='State file for put/diff')
    args = parser.parse_args()



