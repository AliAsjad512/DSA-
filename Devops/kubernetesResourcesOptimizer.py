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
    
    def analyze(self):
        """Compare requests/limits vs actual usage"""
        resources = self.get_pod_resources()
        metrics = self.get_pod_metrics()
        recommendations = []

        for res in resources:
            key = f"{res['pod']}/{res['container']}"
            actual = metrics.get(key, {})
            if not actual:
                continue

            # Parse CPU values (e.g., "100m" -> 0.1)
            cpu_req = self._parse_cpu(res['cpu_request'])
            cpu_lim = self._parse_cpu(res['cpu_limit'])
            cpu_act = self._parse_cpu(actual.get('cpu', '0'))
            mem_req = self._parse_memory(res['memory_request'])
            mem_lim = self._parse_memory(res['memory_limit'])
            mem_act = self._parse_memory(actual.get('memory', '0'))

            issues = []
            if cpu_req > 0 and cpu_act < cpu_req * 0.3:
                issues.append(f"CPU request too high: actual {cpu_act:.2f}c vs {cpu_req:.2f}c")
            if cpu_lim > 0 and cpu_act > cpu_lim * 0.8:
                issues.append(f"CPU limit too low: actual {cpu_act:.2f}c vs {cpu_lim:.2f}c")
            if mem_req > 0 and mem_act < mem_req * 0.3:
                issues.append(f"Memory request too high: actual {mem_act:.0f}Mi vs {mem_req:.0f}Mi")
            if mem_lim > 0 and mem_act > mem_lim * 0.8:
                issues.append(f"Memory limit too low: actual {mem_act:.0f}Mi vs {mem_lim:.0f}Mi")

            if issues:
                recommendations.append({
                    'pod': res['pod'],
                    'container': res['container'],
                    'issues': issues,
                    'suggested_cpu_request': max(0.1, cpu_act * 1.2),
                    'suggested_memory_request': max(128, mem_act * 1.2)
                })

        return recommendations
    @staticmethod
    def _parse_cpu(value):
        if value.endswith('m'):
            return float(value[:-1]) / 1000
        return float(value) if value != '0' else 0

    @staticmethod
    def _parse_memory(value):
        if value.endswith('Ki'):
            return float(value[:-2]) / 1024
        if value.endswith('Mi'):
            return float(value[:-2])
        if value.endswith('Gi'):
            return float(value[:-2]) * 1024
        return float(value) / (1024**2) if value != '0' else 0
    
    if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='K8s Resource Optimizer')
    parser.add_argument('--namespace', default='default')
    args = parser.parse_args()

    optimizer = K8sResourceOptimizer(args.namespace)
    recommendations = optimizer.analyze()
    if recommendations:
        print(f"📊 Resource Optimization Recommendations for namespace '{args.namespace}':")
        for rec in recommendations:
            print(f"\n🔹 {rec['pod']}/{rec['container']}")
            for issue in rec['issues']:
                print(f"   - {issue}")
            print(f"   💡 Suggested CPU request: {rec['suggested_cpu_request']:.2f}c")
            print(f"   💡 Suggested Memory request: {rec['suggested_memory_request']:.0f}Mi")
    else:
        print("✅ No resource optimization needed")

        