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

    def commit(self, message, files=None):
        """Commit changes"""
        if not self.repo_path.exists():
            print("Repository does not exist")
            return
        os.chdir(self.repo_path)
        if files:
            subprocess.run(['git', 'add'] + files, check=True)
        else:
            subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', message], check=True)
        print(f"✅ Committed with message: {message}")
    def push(self, remote='origin', branch='main'):
        """Push changes"""
        os.chdir(self.repo_path)
        subprocess.run(['git', 'push', remote, branch], check=True)
        print(f"✅ Pushed to {remote}/{branch}")
    def pull(self, remote='origin', branch='main'):
        """Pull latest changes"""
        os.chdir(self.repo_path)
        subprocess.run(['git', 'pull', remote, branch], check=True)
        print(f"✅ Pulled latest from {remote}/{branch}")

    def tag(self, tag_name, message=None):
        """Create a tag"""
        os.chdir(self.repo_path)
        cmd = ['git', 'tag', tag_name]
        if message:
            cmd = ['git', 'tag', '-a', tag_name, '-m', message]
        subprocess.run(cmd, check=True)
        print(f"✅ Created tag {tag_name}")