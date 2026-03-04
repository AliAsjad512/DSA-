import psutil
import datetime
import json
import socket
import os
from typing import Dict, Any

class ServerHealthMonitor:
    def __init__(self, threshold_cpu=80, threshold_memory=80, threshold_disk=80):
        self.threshold_cpu = threshold_cpu
        self.threshold_memory = threshold_memory
        self.threshold_disk = threshold_disk
        self.hostname = socket.gethostname()
        
    def get_cpu_usage(self) -> Dict[str, Any]:
        """Get CPU usage statistics"""
        return {
            'percent': psutil.cpu_percent(interval=1),
            'count': psutil.cpu_count(),
            'load_avg': psutil.getloadavg()
        }