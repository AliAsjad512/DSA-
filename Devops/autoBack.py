import os
import shutil
import tarfile
import hashlib
import json
from datetime import datetime, timedelta
from pathlib import Path
import argparse
import logging
from cryptography.fernet import Fernet

class BackupSystem:
    def __init__(self, backup_dir: str = "/backups", retention_days: int = 30):
        self.backup_dir = Path(backup_dir)
        self.retention_days = retention_days
        self.metadata_file = self.backup_dir / "backup_metadata.json"
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('backup_system.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

        self.backup_dir.mkdir(parents=True, exist_ok=True)
        
        # Load or create metadata
        self.metadata = self._load_metadata()
        
    def _load_metadata(self):
        """Load backup metadata from file"""
        if self.metadata_file.exists():
            with open(self.metadata_file, 'r') as f:
                return json.load(f)
        return {'backups': [], 'total_size': 0}
    
    def _save_metadata(self):
        """Save backup metadata to file"""
        with open(self.metadata_file, 'w') as f:
            json.dump(self.metadata, f, indent=2)