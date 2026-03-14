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
         def parse_log_file(self, filepath: str) -> Dict:
        """Parse a single log file"""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File {filepath} not found")
        
        # Handle gzipped files
        open_func = gzip.open if filepath.endswith('.gz') else open
        mode = 'rt' if filepath.endswith('.gz') else 'r'
        
        with open_func(filepath, mode) as f:
            for line_num, line in enumerate(f, 1):
                self._analyze_line(line.strip(), line_num, filepath)
        
        return self.get_summary()
        