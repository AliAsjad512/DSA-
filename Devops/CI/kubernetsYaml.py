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

def generate_report(self):
        """Generate a report of resources found"""
        resource_count = {}
        for doc in self.documents:
            kind = doc.get('kind', 'Unknown')
            resource_count[kind] = resource_count.get(kind, 0) + 1

        images = self.get_images()
        errors = self.validate()

        report = {
            'total_documents': len(self.documents),
            'resource_types': resource_count,
            'images': images,
            'validation_errors': errors
        }
        return report
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Kubernetes YAML Parser')
    parser.add_argument('path', help='File or directory to parse')
    parser.add_argument('--output', help='Output JSON file', default=None)
    args = parser.parse_args()

    parser = K8sYamlParser()
    if os.path.isfile(args.path):
        parser.load_file(args.path)
    elif os.path.isdir(args.path):
        parser.load_directory(args.path)
    else:
        print(f"❌ Path not found: {args.path}")
        sys.exit(1)

    report = parser.generate_report()

    print("\n📊 Kubernetes YAML Report:")
    print(f"  Total documents: {report['total_documents']}")
    print(f"  Resource types: {report['resource_types']}")
    print(f"  Unique images ({len(report['images'])}):")
    for img in report['images']:
        print(f"    - {img}")

    if report['validation_errors']:
        print("\n❌ Validation errors:")
        for err in report['validation_errors']:
            print(f"    - {err}")
    else:
        print("\n✅ No validation errors found.")

    if args.output:
        with open(args.output, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"✅ Report saved to {args.output}")