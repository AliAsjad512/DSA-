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
         def upload_directory(self, directory, compress=False):
        """Upload entire directory recursively"""
        directory = Path(directory)
        if not directory.is_dir():
            self.logger.error(f"{directory} is not a directory")
            return False

        success = True
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = Path(root) / file
                rel_path = file_path.relative_to(directory)
                s3_key = f"{self.prefix}{rel_path}"
                if not self.upload_file(file_path, str(s3_key), compress):
                    success = False
        return success
    
    def list_backups(self):
        """List all backups in the bucket prefix"""
        response = self.s3.list_objects_v2(Bucket=self.bucket, Prefix=self.prefix)
        if 'Contents' not in response:
            print("No backups found")
            return []
        backups = []
        for obj in response['Contents']:
            backups.append({
                'Key': obj['Key'],
                'Size': obj['Size'],
                'LastModified': obj['LastModified']
            })
        return backups
    

     def delete_old_backups(self, days=30):
        """Delete backups older than N days"""
        cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=days)
        backups = self.list_backups()
        deleted = []
        for backup in backups:
            if backup['LastModified'] < cutoff:
                self.s3.delete_object(Bucket=self.bucket, Key=backup['Key'])
                deleted.append(backup['Key'])
                self.logger.info(f"Deleted old backup: {backup['Key']}")
        return deleted
    
    def restore_file(self, s3_key, local_path):
        """Download a file from S3"""
        try:
            self.s3.download_file(self.bucket, s3_key, local_path)
            self.logger.info(f"✅ Restored s3://{self.bucket}/{s3_key} to {local_path}")
            return True
        except Exception as e:
            self.logger.error(f"Restore failed: {e}")
            return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='S3 Backup Manager')
    parser.add_argument('--bucket', required=True, help='S3 bucket')
    parser.add_argument('--prefix', default='backups/', help='S3 prefix')
    parser.add_argument('--region', default='us-east-1', help='AWS region')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Upload
    upload_parser = subparsers.add_parser('upload')
    upload_parser.add_argument('path', help='File or directory to upload')
    upload_parser.add_argument('--compress', action='store_true', help='Compress before upload')