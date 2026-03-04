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
     def get_memory_usage(self) -> Dict[str, Any]:
        """Get memory usage statistics"""
        memory = psutil.virtual_memory()
        return {
            'total': self._bytes_to_gb(memory.total),
            'available': self._bytes_to_gb(memory.available),
            'percent': memory.percent,
            'used': self._bytes_to_gb(memory.used),
            'free': self._bytes_to_gb(memory.free)
        }
    
    def get_disk_usage(self) -> Dict[str, Any]:
        """Get disk usage statistics"""
        disk = psutil.disk_usage('/')
        return {
            'total': self._bytes_to_gb(disk.total),
            'used': self._bytes_to_gb(disk.used),
            'free': self._bytes_to_gb(disk.free),
            'percent': disk.percent
        }