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

               def monitor_pods(self, interval=5):
        """Continuously monitor pod status"""
        print(f"🔍 Monitoring pods in namespace '{self.namespace}' (Ctrl+C to stop)")
        try:
            while True:
                pods = self.get_pods()
                table_data = []
                for pod in pods:
                    name = pod.metadata.name
                    status = pod.status.phase
                    restart_count = sum(cs.restart_count for cs in pod.status.container_statuses or [])
                    age = datetime.datetime.now() - pod.metadata.creation_timestamp.replace(tzinfo=None)
                    age_str = str(age).split('.')[0]  # remove microseconds

                    # Check conditions
                    ready_conditions = [c for c in pod.status.conditions if c.type == 'Ready'] if pod.status.conditions else []
                    ready = 'Yes' if ready_conditions and ready_conditions[0].status == 'True' else 'No'

                    table_data.append([name, status, ready, restart_count, age_str])

                # Clear screen and print table
                print("\033[2J\033[H")  # ANSI clear screen
                print(f"📊 Pod Status in namespace '{self.namespace}' at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                print(tabulate(table_data, headers=['Pod Name', 'Status', 'Ready', 'Restarts', 'Age'], tablefmt='grid'))
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\n🛑 Monitoring stopped")


            def get_unhealthy_pods(self):
        """Return list of pods that are not running"""
        pods = self.get_pods()
        unhealthy = []
        for pod in pods:
            if pod.status.phase != 'Running':
                unhealthy.append(pod)
            else:
                # Check if all containers are ready
                if pod.status.container_statuses:
                    for cs in pod.status.container_statuses:
                        if not cs.ready:
                            unhealthy.append(pod)
                            break
        return unhealthy


        if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Kubernetes Pod Monitor')
    parser.add_argument('--namespace', default='default', help='Kubernetes namespace')
    parser.add_argument('--interval', type=int, default=5, help='Refresh interval (seconds)')
    parser.add_argument('--once', action='store_true', help='Run once and exit (no continuous monitoring)')
    args = parser.parse_args()

    monitor = K8sPodMonitor(namespace=args.namespace)

    if args.once:
        pods = monitor.get_pods()
        table_data = []
        for pod in pods:
            name = pod.metadata.name
            status = pod.status.phase
            restart_count = sum(cs.restart_count for cs in pod.status.container_statuses or [])
            age = datetime.datetime.now() - pod.metadata.creation_timestamp.replace(tzinfo=None)
            age_str = str(age).split('.')[0]
            table_data.append([name, status, restart_count, age_str])

        print(tabulate(table_data, headers=['Pod Name', 'Status', 'Restarts', 'Age'], tablefmt='grid'))