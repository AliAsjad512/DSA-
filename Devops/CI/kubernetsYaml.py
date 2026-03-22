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


                   def load_directory(self, directory):
        """Load all YAML files in a directory"""
        yaml_files = list(Path(directory).glob('*.yaml')) + list(Path(directory).glob('*.yml'))
        for file in yaml_files:
            print(f"📄 Loading {file}")
            self.load_file(file)

            