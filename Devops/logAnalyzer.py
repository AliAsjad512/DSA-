import re
import gzip
from collections import Counter, defaultdict
from datetime import datetime
import os
from typing import List, Dict, Tuple
import argparse

class LogAnalyzer:
    def __init__(self, log_patterns: Dict[str, str] = None):
        self.log_patterns = log_patterns or {
            'ERROR': r'ERROR|error|Error|Exception|Failed|failed',
            'WARNING': r'WARN|WARNING|warning',
            'INFO': r'INFO|info',
            'DEBUG': r'DEBUG|debug'
        }
        self.results = defaultdict(lambda: {
            'count': 0,
            'lines': [],
            'timestamps': []
        })
        