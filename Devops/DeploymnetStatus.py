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

               return {
            'status': status,
            'response_time_ms': response_time,
            'details': details,
            'checked_at': datetime.now().isoformat()
        }
    
    def check_version(self, env_config: Dict) -> Dict:
        """Check deployed version"""
        url = env_config['url'] + env_config.get('version_endpoint', '/version')
        
        try:
            response = requests.get(url, timeout=env_config.get('timeout', 5))
            if response.status_code == 200:
                version_info = response.json()
                current_version = version_info.get('version', 'unknown')
                
                expected = self.config.get('expected_version')
                if expected and current_version == expected:
                    status = DeploymentStatus.SUCCESS
                else:
                    status = DeploymentStatus.FAILED
            else:
                current_version = 'unknown'
                status = DeploymentStatus.UNKNOWN
        except:
            current_version = 'error'
            status = DeploymentStatus.UNKNOWN
        
        return {
            'current_version': current_version,
            'expected_version': self.config.get('expected_version'),
            'status': status,
            'checked_at': datetime.now().isoformat()
        }
    
    def check_all_environments(self) -> Dict:
        """Check all configured environments"""
        for env_name, env_config in self.config['environments'].items():
            print(f"🔍 Checking {env_name.upper()} environment...")
            
            health_result = self.check_health(env_config)
            version_result = self.check_version(env_config)
            
            self.results[env_name] = {
                'health': health_result,
                'version': version_result,
                'overall_status': self._determine_overall_status(health_result, version_result)
            }
               def generate_report(self) -> str:
        """Generate deployment status report"""
        lines = []
        lines.append("=" * 60)
        lines.append("DEPLOYMENT STATUS REPORT")
        lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("=" * 60)
        
        for env_name, result in self.results.items():
            lines.append(f"\n🌍 Environment: {env_name.upper()}")
            lines.append("-" * 40)
            lines.append(f"Overall: {result['overall_status'].value}")
            
            health = result['health']
            lines.append(f"Health: {health['status'].value} ({health['response_time_ms']}ms)")
            
            version = result['version']
            if version['status'] == DeploymentStatus.SUCCESS:
                lines.append(f"Version: {version['current_version']} ✅")
            else:
                lines.append(f"Version: {version['current_version']} (expected: {version['expected_version']})")
        
        return "\n".join(lines)
    
    def send_alert(self, env_name: str, status: DeploymentStatus):
        """Send alert for deployment issues"""
        if status == DeploymentStatus.FAILED:
            print(f"🔔 ALERT: Deployment to {env_name} FAILED!")
            # Here you could integrate with Slack, Email, PagerDuty, etc.
            # Example: send_slack_notification(f"Deployment to {env_name} failed!")


# Usage
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deployment Status Checker")
    parser.add_argument("action", choices=['check', 'monitor', 'report'])
    parser.add_argument("--env", help="Environment to check (dev, staging, production)")
    parser.add_argument("--config", default="deployment_config.json", help="Configuration file")
    parser.add_argument("--interval", type=int, default=5, help="Check interval in seconds")
    
    args = parser.parse_args()
    
    checker = DeploymentChecker(args.config)
    
    if args.action == 'check':
        results = checker.check_all_environments()
        print(checker.generate_report())
    
    elif args.action == 'monitor':
        if not args.env:
            print("❌ --env is required for monitor action")
            sys.exit(1)
        success = checker.monitor_deployment(args.env, args.interval)
        sys.exit(0 if success else 1)
    
    elif args.action == 'report':
        checker.check_all_environments()
        print(checker.generate_report())