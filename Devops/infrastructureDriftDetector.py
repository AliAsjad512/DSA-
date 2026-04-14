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

