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
        container_list = []
        for container in containers:
            container_list.append({
                'id': container.short_id,
                'name': container.name,
                'image': container.image.tags[0] if container.image.tags else 'none',
                'status': container.status,
                'state': container.attrs['State']['Status'],
                'created': datetime.fromtimestamp(container.attrs['Created']).strftime('%Y-%m-%d %H:%M:%S'),
                'ports': self._format_ports(container.attrs['NetworkSettings']['Ports'])
            })

            return container_list
         def _format_ports(self, ports: Dict) -> str:
        """Format port mappings"""
        if not ports:
            return 'none'
        
        port_strs = []
        for container_port, mappings in ports.items():
            if mappings:
                for mapping in mappings:
                    port_strs.append(f"{mapping['HostIp']}:{mapping['HostPort']}->{container_port}")
            else:
                port_strs.append(container_port)
        
        return ', '.join(port_strs)