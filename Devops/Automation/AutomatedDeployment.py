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