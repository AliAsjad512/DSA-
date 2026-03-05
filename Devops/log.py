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
    
    def parse_log_directory(self, directory: str, pattern: str = "*.log") -> Dict:
        """Parse all log files in a directory"""
        import glob
        
        log_files = glob.glob(os.path.join(directory, pattern))
        if not log_files:
            print(f"⚠️ No log files found matching pattern {pattern}")
            return {}
        
        for log_file in log_files:
            print(f"📄 Parsing {log_file}...")
            self.parse_log_file(log_file)
        
        return self.get_summary()
    
     def _analyze_line(self, line: str, line_num: int, filename: str):
        """Analyze a single line of log"""
        for level, pattern in self.log_patterns.items():
            if re.search(pattern, line):
                self.results[level]['count'] += 1
                self.results[level]['lines'].append({
                    'line': line_num,
                    'content': line,
                    'file': filename
                })
                
                # Try to extract timestamp
                timestamp = self._extract_timestamp(line)
                if timestamp:
                    self.results[level]['timestamps'].append(timestamp)
                break
    