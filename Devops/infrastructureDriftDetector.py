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

