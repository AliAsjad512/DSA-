import yaml
import json
import argparse
import os
from pathlib import Path
import sys

class K8sYamlParser:
    def __init__(self):
        self.documents = []

    def load_file(self, filepath):
        """Load and parse a YAML file (can contain multiple documents)"""
        with open(filepath, 'r') as f:
            try:
                docs = list(yaml.safe_load_all(f))
                self.documents.extend(docs)
                return docs
            except yaml.YAMLError as e:
                print(f"❌ YAML parsing error in {filepath}: {e}")
                return None