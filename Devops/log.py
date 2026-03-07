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
     def _extract_timestamp(self, line: str) -> str:
        """Extract timestamp from log line"""
        # Common timestamp patterns
        patterns = [
            r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',
            r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}',
            r'\d{2}:\d{2}:\d{2}'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, line)
            if match:
                return match.group()
        return None
    
    def get_error_frequency(self, top_n: int = 10) -> List[Tuple[str, int]]:
        """Get most frequent error messages"""
        error_lines = [item['content'] for item in self.results['ERROR']['lines']]
        return Counter(error_lines).most_common(top_n)
    
    def get_summary(self) -> Dict:
        """Get analysis summary"""
        summary = {}
        for level, data in self.results.items():
            summary[level] = {
                'count': data['count'],
                'percentage': 0,
                'first_occurrence': min(data['timestamps']) if data['timestamps'] else None,
                'last_occurrence': max(data['timestamps']) if data['timestamps'] else None
            }
        
        # Calculate percentages
        total = sum(data['count'] for data in self.results.values())
        if total > 0:
            for level in summary:
                summary[level]['percentage'] = round(
                    (summary[level]['count'] / total) * 100, 2
                )
        
        return summary
    
    def generate_report(self, output_file: str = None):
        """Generate detailed report"""
        report_lines = []
        report_lines.append("=" * 60)
        report_lines.append("LOG ANALYSIS REPORT")
        report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append("=" * 60)
        
        # Summary
        summary = self.get_summary()
        report_lines.append("\n📊 SUMMARY STATISTICS:")
        for level, data in summary.items():
            report_lines.append(f"  {level}: {data['count']} occurrences ({data['percentage']}%)")
        
        # Error frequency
        if self.results['ERROR']['count'] > 0:
            report_lines.append("\n🔥 TOP ERROR MESSAGES:")
            for error, count in self.get_error_frequency(5):
                report_lines.append(f"  - [{count}x] {error[:100]}...")
        
        # Detailed errors
        report_lines.append("\n📝 DETAILED ERROR LOGS:")
        for item in self.results['ERROR']['lines'][:20]:  # Show first 20
            report_lines.append(f"  [{item['file']}:{item['line']}] {item['content']}")
        
        report = "\n".join(report_lines)
        
        if output_file:
            with open(output_file, 'w') as f:
                f.write(report)
            print(f"✅ Report saved to {output_file}")
        
        return report


# Usage
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Log File Analyzer")
    parser.add_argument("path", help="Log file or directory path")
    parser.add_argument("--pattern", default="*.log", help="File pattern for directories")
    parser.add_argument("--output", help="Output report file")
    
    args = parser.parse_args()
    
    analyzer = LogAnalyzer()
    
    if os.path.isfile(args.path):
        analyzer.parse_log_file(args.path)
    elif os.path.isdir(args.path):
        analyzer.parse_log_directory(args.path, args.pattern)
    else:
        print(f"❌ Invalid path: {args.path}")
        exit(1)
    
    report = analyzer.generate_report(args.output)
    print(report)

    # creating the dataframe using dictionary
store_data = pd.DataFrame({'CustomerID': ['CustID00','CustID01','CustID02','CustID03','CustID04']
                           ,'location': ['Chicago', 'Boston', 'Seattle', 'San Francisco', 'Austin']
                           ,'gender': ['M','M','F','M','F']
                           ,'type': ['Electronics','Food&Beverages','Food&Beverages','Medicine','Beauty']
                           ,'quantity':[1,3,4,2,1],'total_bill':[100,75,125,50,80]})
store_data