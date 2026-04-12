import boto3
import datetime
import json
import argparse
import numpy as np
from collections import defaultdict

class CostAnomalyDetector:
    def __init__(self, region='us-east-1'):
        self.ce = boto3.client('ce', region_name=region)