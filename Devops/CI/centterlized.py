import os
import time
import json
import logging
import socket
import argparse
import threading
import queue
from pathlib import Path
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class LogForwarder(FileSystemEventHandler):
    def __init__(self, log_queue, log_files):
        self.log_queue = log_queue
        self.log_files = set(log_files)
        self.file_handles = {}
        self.file_positions = {}
        self._init_tracking()

         def _init_tracking(self):
        for log_file in self.log_files:
            if os.path.exists(log_file):
                self.file_handles[log_file] = open(log_file, 'r')
                self.file_positions[log_file] = os.path.getsize(log_file)
                self.file_handles[log_file].seek(self.file_positions[log_file])

        def on_modified(self, event):
        if not event.is_directory and event.src_path in self.log_files:
            self._read_new_lines(event.src_path)

     def _read_new_lines(self, filepath):
        f = self.file_handles.get(filepath)
        if not f:
            return
        lines = f.readlines()
        if lines:
            for line in lines:
                self.log_queue.put({
                    'source': filepath,
                    'line': line.strip(),
                    'timestamp': datetime.utcnow().isoformat(),
                    'host': socket.gethostname()
                })
            self.file_positions[filepath] = f.tell()


               def run_initial_read(self):
        for filepath in self.log_files:
            self._read_new_lines(filepath)

class LogProcessor:
    def __init__(self, output_type='stdout', **kwargs):
        self.output_type = output_type
        self.kwargs = kwargs

    def process(self, log_entry):
        if self.output_type == 'stdout':
            print(json.dumps(log_entry))
        elif self.output_type == 'elasticsearch':
            self._send_to_elasticsearch(log_entry)
        elif self.output_type == 'syslog':
            self._send_to_syslog(log_entry)
        elif self.output_type == 'file':
            self._write_to_file(log_entry)
            def _send_to_syslog(self, entry):
        syslog_host = self.kwargs.get('syslog_host', 'localhost')
        syslog_port = self.kwargs.get('syslog_port', 514)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(json.dumps(entry).encode(), (syslog_host, syslog_port))

    def _write_to_file(self, entry):
        output_file = self.kwargs.get('output_file', 'forwarded_logs.json')
        with open(output_file, 'a') as f:
            f.write(json.dumps(entry) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Centralized Log Forwarder')
    parser.add_argument('--logs', nargs='+', required=True, help='Log files to monitor')
    parser.add_argument('--output', choices=['stdout', 'elasticsearch', 'syslog', 'file'], default='stdout')
    parser.add_argument('--es-url', help='Elasticsearch URL')
    parser.add_argument('--syslog-host', default='localhost')
    parser.add_argument('--syslog-port', type=int, default=514)
    parser.add_argument('--output-file', default='forwarded_logs.json')
    args = parser.parse_args()

    log_queue = queue.Queue()
    event_handler = LogForwarder(log_queue, args.logs)
    observer = Observer()
    for log_file in args.logs:
        observer.schedule(event_handler, path=os.path.dirname(log_file), recursive=False)
    observer.start()
    event_handler.run_initial_read()

    processor = LogProcessor(
        output_type=args.output,
        es_url=args.es_url,
        syslog_host=args.syslog_host,
        syslog_port=args.syslog_port,
        output_file=args.output_file
    )

    print(f"✅ Log forwarder started. Monitoring: {args.logs}")
    try:
        while True:
            entry = log_queue.get()
            processor.process(entry)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
        print("\n🛑 Log forwarder stopped")


