import os
import subprocess
import sys
import requests
import json
from pathlib import Path
import getpass

class GitHubPushAutomation:
    def __init__(self):
        self.repo_name = None
        self.github_username = None
        self.repo_path = os.getcwd()
        self.branch_name = "main"

def print_colored(self, text, color='green'):
        """Print colored text for better visibility"""
        colors = {
            'green': '\033[92m',
            'red': '\033[91m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'reset': '\033[0m'
        }
        print(f"{colors.get(color, '')}{text}{colors['reset']}")