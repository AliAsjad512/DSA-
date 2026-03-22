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

 def validate(self):
        """Basic validation of Kubernetes resources"""
        errors = []
        for idx, doc in enumerate(self.documents):
            if not doc:
                continue
            # Check required fields
            if 'apiVersion' not in doc:
                errors.append(f"Document {idx}: missing apiVersion")
            if 'kind' not in doc:
                errors.append(f"Document {idx}: missing kind")
            if 'metadata' not in doc:
                errors.append(f"Document {idx}: missing metadata")
            elif 'name' not in doc['metadata']:
                errors.append(f"Document {idx}: missing metadata.name")

            # Check for common issues
            if doc.get('kind') == 'Deployment':
                spec = doc.get('spec', {})
                if 'replicas' in spec and spec['replicas'] == 0:
                    errors.append(f"Document {idx}: Deployment '{doc['metadata']['name']}' has 0 replicas")
                # Check if image is specified
                template = spec.get('template', {})
                pod_spec = template.get('spec', {})
                containers = pod_spec.get('containers', [])
                for c in containers:
                    if 'image' not in c:
                        errors.append(f"Document {idx}: Container '{c.get('name', 'unknown')}' missing image")
        return errors
 def get_images(self):
        """Extract all container images from the manifests"""
        images = set()
        for doc in self.documents:
            if not doc:
                continue
            kind = doc.get('kind')
            if kind in ['Deployment', 'StatefulSet', 'DaemonSet', 'Job', 'CronJob']:
                spec = doc.get('spec', {})
                if kind == 'CronJob':
                    spec = spec.get('jobTemplate', {}).get('spec', {})
                template = spec.get('template', {})
                pod_spec = template.get('spec', {})
                containers = pod_spec.get('containers', [])
                for c in containers:
                    if 'image' in c:
                        images.add(c['image'])
                init_containers = pod_spec.get('initContainers', [])
                for c in init_containers:
                    if 'image' in c:
                        images.add(c['image'])
            elif kind == 'Pod':
                spec = doc.get('spec', {})
                containers = spec.get('containers', [])
                for c in containers:
                    if 'image' in c:
                        images.add(c['image'])
        return sorted(images)