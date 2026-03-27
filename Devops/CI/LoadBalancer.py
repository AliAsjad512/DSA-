import argparse
import yaml
import os
from jinja2 import Template

lass HAProxyConfigGenerator:
    def __init__(self, template_file=None):
        self.template_file = template_file or self.default_template()
        self.template = None

    def default_template(self):
        return 
global
    daemon
    maxconn 4096

defaults
    mode http
    timeout connect 5000ms
    timeout client 50000ms
    timeout server 50000ms

frontend http-in
    bind *:80
    {% for frontend in frontends %}
    acl is_{{ frontend.name }} hdr(host) -i {{ frontend.domain }}
    use_backend {{ frontend.name }} if is_{{ frontend.name }}
    {% endfor %}
    default_backend default

{% for backend in backends %}
backend {{ backend.name }}
    balance {{ backend.balance|default('roundrobin') }}
    {% for server in backend.servers %}
    server {{ server.name }} {{ server.host }}:{{ server.port }} check
    {% endfor %}
{% endfor %}

    def load_config(self, config_file):
        """Load YAML configuration"""
        with open(config_file, 'r') as f:
            return yaml.safe_load(f)
        
          def generate(self, config):
        """Generate HAProxy config from YAML data"""
        template = Template(self.template_file)
        return template.render(**config)

def save_config(self, content, output_file):
        """Save generated config to file"""
        with open(output_file, 'w') as f:
            f.write(content)
        print(f"✅ HAProxy config saved to {output_file}")


        if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='HAProxy Config Generator')
    parser.add_argument('config', help='YAML configuration file')
    parser.add_argument('--output', default='haproxy.cfg', help='Output file')
    parser.add_argument('--template', help='Custom Jinja2 template')
    args = parser.parse_args()

    generator = HAProxyConfigGenerator(args.template)
    data = generator.load_config(args.config)
    config_content = generator.generate(data)
    generator.save_config(config_content, args.output)
