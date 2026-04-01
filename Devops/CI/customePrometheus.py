from prometheus_client import start_http_server, Gauge, Counter, Histogram
import time
import random
import psutil
import threading

class MetricsExporter:
    def __init__(self, port=8000):
        self.port = port
        # Define metrics
        self.cpu_usage = Gauge('system_cpu_usage_percent', 'CPU usage percentage')
        self.memory_usage = Gauge('system_memory_usage_percent', 'Memory usage percentage')
        self.request_count = Counter('http_requests_total', 'Total HTTP requests')
        self.request_duration = Histogram('http_request_duration_seconds', 'HTTP request duration')