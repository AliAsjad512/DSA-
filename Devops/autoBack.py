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