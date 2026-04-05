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