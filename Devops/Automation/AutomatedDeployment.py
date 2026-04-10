import subprocess
import json
import argparse
import time
import os
import shutil
import requests
from datetime import datetime

class DeploymentManager:
    def __init__(self, app_name, deploy_dir='/var/www', backup_dir='/var/backups'):
        self.app_name = app_name
        self.deploy_dir = Path(deploy_dir) / app_name
        self.backup_dir = Path(backup_dir) / app_name
        self.current_symlink = self.deploy_dir / 'current'
        self.releases_dir = self.deploy_dir / 'releases'
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        self.releases_dir.mkdir(parents=True, exist_ok=True)

     def create_backup(self):
        """Backup current release if exists"""
        if self.current_symlink.exists() and self.current_symlink.is_symlink():
            version = os.path.basename(os.readlink(self.current_symlink))
            backup_path = self.backup_dir / f"{version}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            shutil.copytree(self.current_symlink, backup_path)
            print(f"✅ Backup created at {backup_path}")
            return str(backup_path)
        return None