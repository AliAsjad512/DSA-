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
