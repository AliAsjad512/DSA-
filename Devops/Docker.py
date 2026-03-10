import docker
import argparse
from datetime import datetime
import json
import sys
from typing import Dict, List, Optional
import tabulate
class DockerManager:
    def __init__(self):
        try:
            self.client = docker.from_env()
            self.api_client = docker.APIClient()
            print("✅ Connected to Docker daemon")
        except Exception as e:
            print(f"❌ Failed to connect to Docker: {e}")
            sys.exit(1)
            def list_containers(self, all_containers: bool = False) -> List[Dict]:
        """List all containers"""
        containers = self.client.containers.list(all=all_containers)