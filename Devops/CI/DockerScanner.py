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