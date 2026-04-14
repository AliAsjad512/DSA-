import subprocess
import json
import argparse
import boto3
from deepdiff import DeepDiff

class DriftDetector:
    def __init__(self, tf_state_path='terraform.tfstate'):
        self.tf_state_path = tf_state_path
        self.tf_state = self._load_tf_state()

    def _load_tf_state(self):
        with open(self.tf_state_path, 'r') as f:
            return json.load(f)
    def get_resources_from_tf(self, resource_type):
        """Extract resources of a specific type from Terraform state"""
        resources = []
        for resource in self.tf_state.get('resources', []):
            if resource['type'] == resource_type:
                for instance in resource.get('instances', []):
                    resources.append({
                        'id': instance['attributes'].get('id'),
                        'attributes': instance['attributes']
                    })
        return resources
    def get_live_s3_buckets(self):
        """Fetch actual S3 buckets from AWS"""
        s3 = boto3.client('s3')
        buckets = s3.list_buckets()['Buckets']
        live = {}
        for bucket in buckets:
            name = bucket['Name']
            # Get bucket tags
            try:
                tags = s3.get_bucket_tagging(Bucket=name)
                tag_dict = {t['Key']: t['Value'] for t in tags.get('TagSet', [])}
            except:
                tag_dict = {}
            live[name] = {
                'name': name,
                'creation_date': bucket['CreationDate'].isoformat(),
                'tags': tag_dict
            }
        return live
    def get_live_ec2_instances(self):
        """Fetch actual EC2 instances from AWS"""
        ec2 = boto3.client('ec2')
        instances = ec2.describe_instances()
        live = {}
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                live[instance_id] = {
                    'id': instance_id,
                    'type': instance['InstanceType'],
                    'state': instance['State']['Name'],
                    'tags': {t['Key']: t['Value'] for t in instance.get('Tags', [])}
                }
        return live
    def detect_drift(self):
        """Compare TF state with live resources"""
        drift_report = {}

        # Check S3 buckets
        tf_buckets = {r['attributes']['bucket']: r['attributes'] for r in self.get_resources_from_tf('aws_s3_bucket')}
        live_buckets = self.get_live_s3_buckets()
        for bucket_name, tf_attrs in tf_buckets.items():
            if bucket_name not in live_buckets:
                drift_report[f"s3_bucket/{bucket_name}"] = {'status': 'missing', 'details': 'Bucket not found in AWS'}
            else:
                # Compare tags
                tf_tags = tf_attrs.get('tags', {})
                live_tags = live_buckets[bucket_name]['tags']
                if tf_tags != live_tags:
                    drift_report[f"s3_bucket/{bucket_name}"] = {
                        'status': 'drifted',
                        'details': f"Tags mismatch: tf={tf_tags}, live={live_tags}"
                    }

        # Check EC2 instances
        tf_instances = {r['attributes']['id']: r['attributes'] for r in self.get_resources_from_tf('aws_instance')}
        live_instances = self.get_live_ec2_instances()
        for instance_id, tf_attrs in tf_instances.items():
            if instance_id not in live_instances:
                drift_report[f"ec2_instance/{instance_id}"] = {'status': 'missing'}
            else:
                live = live_instances[instance_id]
                if tf_attrs.get('instance_type') != live['type']:
                    drift_report[f"ec2_instance/{instance_id}"] = {
                        'status': 'drifted',
                        'details': f"Type mismatch: tf={tf_attrs.get('instance_type')}, live={live['type']}"
                    }

        return drift_report
    
    if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Infrastructure Drift Detector')
    parser.add_argument('--tfstate', default='terraform.tfstate')
    args = parser.parse_args()

    detector = DriftDetector(args.tfstate)
    drift = detector.detect_drift()
    if drift:
        print("⚠️ Infrastructure Drift Detected:")
        for resource, info in drift.items():
            print(f"  - {resource}: {info['status']}")
            if 'details' in info:
                print(f"    {info['details']}")
    else:
        print("✅ No drift detected")



