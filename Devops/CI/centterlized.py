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
            self._write_to_file(log_entr

