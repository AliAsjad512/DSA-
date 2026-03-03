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

         def run_command(self, command):
        """Run shell command and return output"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                check=True
            )
            self.print_colored(f"✓ {command}", 'green')
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            self.print_colored(f"✗ Error in: {command}", 'red')
            print(f"Error details: {e.stderr}")
            return None
    
    def check_git_installed(self):
        """Check if git is installed"""
        try:
            subprocess.run(['git', '--version'], capture_output=True, check=True)
            self.print_colored("✓ Git is installed", 'green')
            return True
        except:
            self.print_colored("✗ Git is not installed!", 'red')
            print("Please install Git from: https://git-scm.com/downloads")
            return False
    
    def initialize_git(self):
        """Initialize git repository if not already initialized"""
        if not os.path.exists(os.path.join(self.repo_path, '.git')):
            self.print_colored("Initializing git repository...", 'yellow')