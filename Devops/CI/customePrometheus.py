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

        def collect_system_metrics(self):
        """Background thread to collect system metrics"""
        while True:
            self.cpu_usage.set(psutil.cpu_percent())
            self.memory_usage.set(psutil.virtual_memory().percent)
            time.sleep(15)

        def simulate_http_traffic(self):
        """Simulate HTTP requests to test metrics"""
        while True:
            duration = random.uniform(0.1, 1.5)
            self.request_duration.observe(duration)
            self.request_count.inc()
            time.sleep(random.randint(5, 30))