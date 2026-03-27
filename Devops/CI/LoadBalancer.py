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