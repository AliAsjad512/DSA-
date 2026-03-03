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