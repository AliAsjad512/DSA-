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

     def get_pod_resources(self):
        """Get all pods with their resource requests and limits"""
        pods = self.core_v1.list_namespaced_pod(self.namespace)
        results = []
        for pod in pods:
            if pod.status.phase != 'Running':
                continue
            for container in pod.spec.containers:
                resources = container.resources
                req = resources.requests if resources and resources.requests else {}
                lim = resources.limits if resources and resources.limits else {}
                results.append({
                    'pod': pod.metadata.name,
                    'container': container.name,
                    'cpu_request': req.get('cpu', '0'),
                    'cpu_limit': lim.get('cpu', '0'),
                    'memory_request': req.get('memory', '0'),
                    'memory_limit': lim.get('memory', '0')
                })
        return results