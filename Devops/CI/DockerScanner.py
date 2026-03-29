import subprocess
import json
import argparse
import sys
import os

class DockerImageScanner:
    def __init__(self, image_name):
        self.image_name = image_name

        def scan_with_trivy(self):
        """Use Trivy to scan image"""
        try:
            result = subprocess.run(
                ['trivy', 'image', '--format', 'json', '--no-progress', self.image_name],
                capture_output=True,
                text=True,
                check=True
            )
            return json.loads(result.stdout)
        except FileNotFoundError:
            print("Trivy not installed. Install from https://github.com/aquasecurity/trivy")
            return None
        except subprocess.CalledProcessError as e:
            print(f"Trivy scan failed: {e.stderr}")
            return None
        
        def scan_with_docker_scan(self):
        """Use Docker Scan (Snyk)"""
        try:
            result = subprocess.run(
                ['docker', 'scan', self.image_name, '--json'],
                capture_output=True,
                text=True,
                check=True
            )
            return json.loads(result.stdout)
        except:
            return None
        
        def extract_layers(self):
        """Extract image layers and inspect content (simple)"""
        try:
            result = subprocess.run(
                ['docker', 'history', self.image_name, '--format', '{{.CreatedBy}}'],
                capture_output=True,
                text=True,
                check=True
            )
            layers = [line.strip() for line in result.stdout.split('\n') if line.strip()]
            return layers
        except:
            return []
        
        def generate_report(self):
        """Generate security report"""
        report = {
            'image': self.image_name,
            'vulnerabilities': []
        }
        trivy_report = self.scan_with_trivy()
        if trivy_report:
            for result in trivy_report.get('Results', []):
                for vuln in result.get('Vulnerabilities', []):
                    report['vulnerabilities'].append({
                        'title': vuln.get('Title'),
                        'severity': vuln.get('Severity'),
                        'package': vuln.get('PkgName'),
                        'installed_version': vuln.get('InstalledVersion'),
                        'fixed_version': vuln.get('FixedVersion'),
                        'description': vuln.get('Description')
                    })
        return report
    
    if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Docker Image Scanner')
    parser.add_argument('image', help='Docker image name')
    parser.add_argument('--output', help='Output JSON file')
    args = parser.parse_args()

    scanner = DockerImageScanner(args.image)
    report = scanner.generate_report()

    print(f"🔍 Security scan for {args.image}")
    print("=" * 60)
    print(f"Vulnerabilities found: {len(report['vulnerabilities'])}")
    # Group by severity