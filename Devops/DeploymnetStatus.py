#!/usr/bin/env python3
"""
Deployment Status Checker - Monitor deployment status across environments
"""

import requests
import time
from datetime import datetime
from typing import Dict, List, Optional
import json
import argparse
import sys
from enum import Enum

class DeploymentStatus(Enum):
    SUCCESS = "✅ SUCCESS"
    FAILED = "❌ FAILED"
    IN_PROGRESS = "⏳ IN PROGRESS"
    PENDING = "⏸️ PENDING"
    UNKNOWN = "❓ UNKNOWN
    class DeploymentChecker:
    def __init__(self, config_file: str = "deployment_config.json"):
        self.config = self._load_config(config_file)
        self.results = {}
        
    def _load_config(self, config_file: str) -> Dict:
        """Load deployment configuration"""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            # Default configuration
            return {
                "environments": {
                    "dev": {
                        "url": "http://dev.example.com",
                        "health_endpoint": "/health",
                        "version_endpoint": "/version",
                        "timeout": 5
                    },
                    "staging": {
                        "url": "http://staging.example.com",
                        "health_endpoint": "/health",
                        "version_endpoint": "/version",
                        "timeout": 5
                    },
                    "production": {
                        "url": "http://example.com",
                        "health_endpoint": "/health",
                        "version_endpoint": "/version",
                        "timeout": 5
                    }
                },
                "expected_version": "1.0.0",
                "services": ["api", "web", "database"]
            }
        def check_health(self, env_config: Dict) -> Dict:
        """Check health of a deployment"""
        url = env_config['url'] + env_config['health_endpoint']
        start_time = time.time()
        
        try:
            response = requests.get(
                url,
                timeout=env_config.get('timeout', 5),
                headers={'User-Agent': 'Deployment-Checker/1.0'}
            )
            response_time = round((time.time() - start_time) * 1000, 2)
            
            if response.status_code == 200:
                status = DeploymentStatus.SUCCESS
                details = response.json() if response.text else {}
            else:
                status = DeploymentStatus.FAILED
                details = {'status_code': response.status_code}
                
        except requests.exceptions.Timeout:
            status = DeploymentStatus.FAILED
            response_time = env_config.get('timeout', 5) * 1000
            details = {'error': 'Timeout'}
        except requests.exceptions.ConnectionError:
            status = DeploymentStatus.FAILED
            response_time = 0
            details = {'error': 'Connection Error'}
        except Exception as e:
            status = DeploymentStatus.FAILED
            response_time = 0
            details = {'error': str(e)}