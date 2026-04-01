from prometheus_client import start_http_server, Gauge, Counter, Histogram
import time
import random
import psutil
import threading

class MetricsExporter: