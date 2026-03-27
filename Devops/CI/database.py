import subprocess
import argparse
import os
import sys
from pathlib import Path
import yaml
import logging

class MigrationRunner:
    def __init__(self, config_file='alembic.ini', env='development'):
        self.config_file = config_file
        self.env = env
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

         def run_migration(self, revision='head'):
        """Run alembic upgrade"""
        try:
            subprocess.run(
                ['alembic', '-c', self.config_file, 'upgrade', revision],
                check=True,
                capture_output=True,
                text=True
            )
            self.logger.info(f"✅ Migration to {revision} succeeded")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Migration failed: {e.stderr}")
            sys.exit(1)

             def create_migration(self, message, autogenerate=True):
        """Create a new migration"""
        cmd = ['alembic', '-c', self.config_file, 'revision', '--autogenerate' if autogenerate else '', '-m', message]
        cmd = [c for c in cmd if c]  # remove empty
        try:
            subprocess.run(cmd, check=True)
            self.logger.info(f"✅ Created migration: {message}")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to create migration: {e.stderr}")
            sys.exit(1)