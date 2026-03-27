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

            def show_history(self):
        """Show migration history"""
        subprocess.run(['alembic', '-c', self.config_file, 'history'])

          def downgrade(self, revision='-1'):
        """Downgrade database"""
        try:
            subprocess.run(
                ['alembic', '-c', self.config_file, 'downgrade', revision],
                check=True
            )
            self.logger.info(f"✅ Downgraded to {revision}")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Downgrade failed: {e.stderr}")
            sys.exit(1)

def current_version(self):
        """Show current database revision"""
        result = subprocess.run(
            ['alembic', '-c', self.config_file, 'current'],
            capture_output=True,
            text=True
        )
        print(result.stdout)

    def run_with_env(self, env_config):
        """Set environment variables before running migrations"""
        # Load environment-specific config from yaml
        if env_config:
            with open(env_config, 'r') as f:
                env_data = yaml.safe_load(f).get(self.env, {})
            for key, value in env_data.items():
                os.environ[key] = str(value)
        # Then run migration
        self.run_migration()
