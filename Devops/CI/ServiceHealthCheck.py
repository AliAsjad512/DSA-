import subprocess
import time
import argparse
import logging
import sys
from datetime import datetime
import requests
import socket


class ServiceHealthMonitor:
    def __init__(self, service_name, check_interval=30, max_failures=3):
        self.service_name = service_name
        self.check_interval = check_interval
        self.max_failures = max_failures
        self.failure_count = 0
        self.setup_logging()
def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(f'/var/log/{self.service_name}_monitor.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(self.service_name)


        def check_process(self, process_name=None):
        """Check if process is running"""
        name = process_name or self.service_name
        try:
            result = subprocess.run(['pgrep', '-f', name], capture_output=True, text=True)
            if result.returncode == 0:
                return True, result.stdout.strip()
            return False, None
        except Exception as e:
            return False, str(e)
        

         def check_http(self, url, expected_status=200, timeout=5):
        """Check HTTP endpoint"""
        try:
            resp = requests.get(url, timeout=timeout)
            if resp.status_code == expected_status:
                return True, resp.status_code
            return False, resp.status_code
        except Exception as e:
            return False, str(e)
        
        def check_tcp_port(self, host, port):
        """Check TCP port connectivity"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            result = sock.connect_ex((host, port))
            sock.close()
            return result == 0, result
        except Exception as e:
            return False, str(e)
        

        def restart_service(self, restart_cmd=None):
        """Restart the service"""
        if not restart_cmd:
            # Try common service managers
            for cmd in [f'systemctl restart {self.service_name}',
                        f'service {self.service_name} restart',
                        f'supervisorctl restart {self.service_name}']:
                try:
                    subprocess.run(cmd.split(), check=True, capture_output=True)
                    self.logger.info(f"✅ Restarted service using: {cmd}")
                    return True
                except:
                    continue
        else:
            try:
                subprocess.run(restart_cmd.split(), check=True)
                self.logger.info(f"✅ Restarted service using: {restart_cmd}")
                return True
            except:
                pass
        self.logger.error("❌ Failed to restart service")
        return False


 def monitor(self, check_type='process', **kwargs):
        """Main monitoring loop"""
        self.logger.info(f"Starting monitor for {self.service_name} (interval={self.check_interval}s)")

        while True:
            if check_type == 'process':
                alive, details = self.check_process(kwargs.get('process_name'))
            elif check_type == 'http':
                alive, details = self.check_http(kwargs['url'], kwargs.get('expected_status', 200))
            elif check_type == 'tcp':
                alive, details = self.check_tcp_port(kwargs['host'], kwargs['port'])
            else:
                self.logger.error(f"Unknown check type: {check_type}")
                return

            if alive:
                if self.failure_count > 0:
                    self.logger.info(f"Service recovered after {self.failure_count} failures")
                self.failure_count = 0
                self.logger.debug(f"Service {self.service_name} is healthy ({details})")
            else:
                self.failure_count += 1
                self.logger.warning(f"Service unhealthy (failure {self.failure_count}/{self.max_failures}): {details}")
                if self.failure_count >= self.max_failures:
                    self.logger.warning(f"⚠️ Restarting {self.service_name}...")
                    if self.restart_service(kwargs.get('restart_cmd')):
                        self.failure_count = 0
                        time.sleep(5)  # Wait for service to stabilize
                    else:
                        self.logger.critical(f"Failed to restart {self.service_name}")
                        # Send alert
                        self.send_alert()

            time.sleep(self.check_interval)

    def send_alert(self):
        """Send alert (Slack, email, etc.)"""
        # Implement as needed
        print(f"🔔 ALERT: {self.service_name} failed to restart!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Service Health Monitor')
    parser.add_argument('service', help='Service name')
    parser.add_argument('--check-type', choices=['process', 'http', 'tcp'], default='process')
    parser.add_argument('--interval', type=int, default=30, help='Check interval (seconds)')
    parser.add_argument('--max-failures', type=int, default=3, help='Failures before restart')
    parser.add_argument('--process-name', help='Process name to match (default: service name)')
    parser.add_argument('--url', help='HTTP URL to check')
    parser.add_argument('--host', help='TCP host')
    parser.add_argument('--port', type=int, help='TCP port')
    parser.add_argument('--restart-cmd', help='Custom restart command')
    args = parser.parse_args()

    monitor = ServiceHealthMonitor(args.service, args.interval, args.max_failures)
    kwargs = {}
    if args.process_name:
        kwargs['process_name'] = args.process_name
    if args.url:
        kwargs['url'] = args.url
    if args.host and args.port:
        kwargs['host'] = args.host
        kwargs['port'] = args.port
    if args.restart_cmd:
        kwargs['restart_cmd'] = args.restart_cmd

    monitor.monitor(check_type=args.check_type, **kwargs)
