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

        def upload_file(self, local_path, s3_key=None, compress=False):
        """Upload a file to S3, optionally compress"""
        local_path = Path(local_path)
        if not local_path.exists():
            self.logger.error(f"File {local_path} does not exist")
            return False

        if compress:
            compressed_path = local_path.with_suffix(local_path.suffix + '.gz')
            with open(local_path, 'rb') as f_in:
                with gzip.open(compressed_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            upload_path = compressed_path
            s3_key = s3_key or f"{self.prefix}{local_path.name}.gz"
        else:
            upload_path = local_path
            s3_key = s3_key or f"{self.prefix}{local_path.name}"

        try:
            self.s3.upload_file(str(upload_path), self.bucket, s3_key)
            self.logger.info(f"✅ Uploaded {upload_path} to s3://{self.bucket}/{s3_key}")
            if compress:
                os.remove(compressed_path)
            return True
        except Exception as e:
            self.logger.error(f"Upload failed: {e}")
            return False