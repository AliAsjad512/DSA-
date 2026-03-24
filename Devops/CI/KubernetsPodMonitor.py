"""
Kubernetes Pod Monitor - Watch pod status and restart counts
"""

from kubernetes import client, config
from kubernetes.client.rest import ApiException
import argparse
import time
import datetime
from tabulate import tabulate
class K8sPodMonitor:
    def __init__(self, namespace='default'):
        self.namespace = namespace
        # Load kubeconfig (assumes ~/.kube/config or in-cluster config)
        try:
            config.load_incluster_config()
        except config.ConfigException:
            config.load_kube_config()
        self.v1 = client.CoreV1Api()

        def get_pods(self):
        """Get all pods in namespace"""
        try:
            pods = self.v1.list_namespaced_pod(namespace=self.namespace)
            return pods.items
        except ApiException as e:
            print(f"❌ Kubernetes API error: {e}")
            return []

