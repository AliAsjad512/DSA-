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