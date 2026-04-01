import os
import subprocess
import argparse
import shutil
from pathlib import Path

class GitAutomation:
    def __init__(self, repo_path=None):
        self.repo_path = Path(repo_path) if repo_path else Path.cwd()

    def clone(self, url, branch='main'):
        """Clone a repository"""
        try:
            subprocess.run(['git', 'clone', '-b', branch, url, str(self.repo_path)], check=True)
            print(f"✅ Cloned {url} to {self.repo_path}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Clone failed: {e}")