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