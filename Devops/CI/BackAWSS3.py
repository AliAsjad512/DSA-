import boto3
import os
import argparse
import datetime
import gzip
import shutil
import hashlib
import logging
from pathlib import Path

class S3Backup:
    def __init__(self, bucket, prefix='backups/', region='us-east-1'):
        self.bucket = bucket
        self.prefix = prefix.rstrip('/') + '/'
        self.s3 = boto3.client('s3', region_name=region)
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')