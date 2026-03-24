"""
Kubernetes Pod Monitor - Watch pod status and restart counts
"""

from kubernetes import client, config
from kubernetes.client.rest import ApiException
import argparse
import time
import datetime
from tabulate import tabulate
