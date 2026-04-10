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
    def deploy(self, source_url, version_tag=None, health_check_url=None):
        """Deploy new version"""
        # Create release directory
        release_name = version_tag or datetime.now().strftime('%Y%m%d_%H%M%S')
        release_path = self.releases_dir / release_name
        release_path.mkdir()

        # Clone/Download source
        print(f"📦 Fetching source from {source_url}")
        if source_url.startswith('git@') or source_url.startswith('https://'):
            subprocess.run(['git', 'clone', '--depth', '1', source_url, str(release_path)], check=True)
        else:
            # Assume local directory
            shutil.copytree(source_url, release_path, dirs_exist_ok=True)

        # Run build steps if any
        if (release_path / 'build.sh').exists():
            subprocess.run(['bash', 'build.sh'], cwd=release_path, check=True)

        # Backup current
        backup = self.create_backup()

        # Switch symlink
        new_symlink = self.current_symlink
        temp_symlink = self.deploy_dir / 'current_new'
        temp_symlink.unlink(missing_ok=True)
        temp_symlink.symlink_to(release_path)
        temp_symlink.rename(new_symlink)

        # Health check
        if health_check_url:
            print(f"🔍 Running health check on {health_check_url}")
            time.sleep(5)  # Wait for app to start
            try:
                resp = requests.get(health_check_url, timeout=10)
                if resp.status_code != 200:
                    raise Exception(f"Health check failed: {resp.status_code}")
                print("✅ Health check passed")
            except Exception as e:
                print(f"❌ Health check failed: {e}")
                # Rollback
                self.rollback(backup)
                return False

        # Cleanup old releases (keep last 5)
        releases = sorted(self.releases_dir.iterdir(), key=os.path.getmtime)
        for old_release in releases[:-5]:
            shutil.rmtree(old_release)
            print(f"🗑️ Removed old release {old_release.name}")

        print(f"✅ Deployment of {release_name} successful")
        return True
    def deploy(self, source_url, version_tag=None, health_check_url=None):
        """Deploy new version"""
        # Create release directory
        release_name = version_tag or datetime.now().strftime('%Y%m%d_%H%M%S')
        release_path = self.releases_dir / release_name
        release_path.mkdir()

        # Clone/Download source
        print(f"📦 Fetching source from {source_url}")
        if source_url.startswith('git@') or source_url.startswith('https://'):
            subprocess.run(['git', 'clone', '--depth', '1', source_url, str(release_path)], check=True)
        else:
            # Assume local directory
            shutil.copytree(source_url, release_path, dirs_exist_ok=True)

        # Run build steps if any
        if (release_path / 'build.sh').exists():
            subprocess.run(['bash', 'build.sh'], cwd=release_path, check=True)

        # Backup current
        backup = self.create_backup()

        # Switch symlink
        new_symlink = self.current_symlink
        temp_symlink = self.deploy_dir / 'current_new'
        temp_symlink.unlink(missing_ok=True)
        temp_symlink.symlink_to(release_path)
        temp_symlink.rename(new_symlink)

        # Health check
        if health_check_url:
            print(f"🔍 Running health check on {health_check_url}")
            time.sleep(5)  # Wait for app to start
            try:
                resp = requests.get(health_check_url, timeout=10)
                if resp.status_code != 200:
                    raise Exception(f"Health check failed: {resp.status_code}")
                print("✅ Health check passed")
            except Exception as e:
                print(f"❌ Health check failed: {e}")
                # Rollback
                self.rollback(backup)
                return False

        # Cleanup old releases (keep last 5)
        releases = sorted(self.releases_dir.iterdir(), key=os.path.getmtime)
        for old_release in releases[:-5]:
            shutil.rmtree(old_release)
            print(f"🗑️ Removed old release {old_release.name}")

        print(f"✅ Deployment of {release_name} successful")
        return True
   def rollback(self, backup_path=None):
        """Rollback to previous version"""
        if backup_path:
            # Restore from backup
            backup_path = Path(backup_path)
            rollback_name = f"rollback_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            rollback_path = self.releases_dir / rollback_name
            shutil.copytree(backup_path, rollback_path)
            self.current_symlink.unlink()
            self.current_symlink.symlink_to(rollback_path)
            print(f"✅ Rolled back to {backup_path.name}")
        else:
            # Use previous release
            releases = sorted(self.releases_dir.iterdir(), key=os.path.getmtime)
            if len(releases) >= 2:
                prev_release = releases[-2]
                self.current_symlink.unlink()
                self.current_symlink.symlink_to(prev_release)
                print(f"✅ Rolled back to {prev_release.name}")
            else:
                print("❌ No previous release to rollback to")


