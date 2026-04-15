import boto3
import secrets
import string
import json
import argparse
import logging
from datetime import datetime

class SecretsRotator:
    def __init__(self, region='us-east-1'):
        self.sm = boto3.client('secretsmanager', region_name=region)
        self.rds = boto3.client('rds', region_name=region)
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    def generate_password(self, length=32):
        """Generate a strong random password"""
        alphabet = string.ascii_letters + string.digits + "!@#$%^&*()_+"
        return ''.join(secrets.choice(alphabet) for _ in range(length))
    def get_secret(self, secret_id):
        """Retrieve current secret value"""
        response = self.sm.get_secret_value(SecretId=secret_id)
        return json.loads(response['SecretString'])
    def update_secret(self, secret_id, secret_value):
        """Update secret with new value"""
        self.sm.put_secret_value(
            SecretId=secret_id,
            SecretString=json.dumps(secret_value),
            VersionStages=['AWSCURRENT']
        )
        self.logger.info(f"Updated secret {secret_id}")
    def rotate_rds_password(self, db_instance_id, username, secret_id):
        """Rotate RDS master password and update secrets manager"""
        new_password = self.generate_password()
        # Update RDS
        self.rds.modify_db_instance(
            DBInstanceIdentifier=db_instance_id,
            MasterUserPassword=new_password,
            ApplyImmediately=True
        )
        self.logger.info(f"Updated RDS {db_instance_id} password")
        # Wait for modification to complete
        waiter = self.rds.get_waiter('db_instance_available')
        waiter.wait(DBInstanceIdentifier=db_instance_id)
        # Update secret
        current_secret = self.get_secret(secret_id)
        current_secret['password'] = new_password
        current_secret['rotated_at'] = datetime.utcnow().isoformat()
        self.update_secret(secret_id, current_secret)
        self.logger.info(f"Rotated secret {secret_id} for RDS {db_instance_id}")
    def rotate_api_key(self, secret_id, new_key_prefix="ak_"):
        """Rotate generic API key"""
        new_key = f"{new_key_prefix}{secrets.token_hex(16)}"
        current = self.get_secret(secret_id)
        old_key = current.get('api_key')
        current['api_key'] = new_key
        current['previous_api_key'] = old_key
        current['rotated_at'] = datetime.utcnow().isoformat()
        self.update_secret(secret_id, current)
        self.logger.info(f"Rotated API key for {secret_id}")
    def schedule_rotation(self, secret_id, rotation_days=30):
        """Schedule automatic rotation using Lambda (requires pre-configured rotation lambda)"""
        self.sm.rotate_secret(
            SecretId=secret_id,
            RotationLambdaARN=f"arn:aws:lambda:us-east-1:123456789012:function:{secret_id}_rotator",
            RotationRules={'AutomaticallyAfterDays': rotation_days}
        )
        self.logger.info(f"Scheduled rotation for {secret_id} every {rotation_days} days")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Secrets Rotation')
    parser.add_argument('--action', choices=['rotate-rds', 'rotate-api', 'schedule'], required=True)
    parser.add_argument('--secret-id', required=True)
    parser.add_argument('--db-instance', help='RDS instance ID (for rotate-rds)')
    parser.add_argument('--db-username', help='RDS master username')
    parser.add_argument('--rotation-days', type=int, default=30)
    args = parser.parse_args()

    rotator = SecretsRotator()
    if args.action == 'rotate-rds':
        rotator.rotate_rds_password(args.db_instance, args.db_username, args.secret_id)
    elif args.action == 'rotate-api':
        rotator.rotate_api_key(args.secret_id)
    elif args.action == 'schedule':
        rotator.schedule_rotation(args.secret_id, args.rotation_days)