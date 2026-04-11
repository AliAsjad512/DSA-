from kubernetes import client, config
import argparse
import json
from datetime import datetime

class K8sResourceOptimizer:
    def __init__(self, namespace='default'):
        self.namespace = namespace
        config.load_kube_config()
        self.core_v1 = client.CoreV1Api()
        self.metrics_v1 = client.CustomObjectsApi()