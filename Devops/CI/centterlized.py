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