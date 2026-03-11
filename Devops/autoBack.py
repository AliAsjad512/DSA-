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

            def _calculate_checksum(self, filepath: Path) -> str:
        """Calculate MD5 checksum of a file"""
        hash_md5 = hashlib.md5()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def _get_file_size(self, path: Path) -> int:
        """Get size of file or directory"""
        if path.is_file():
            return path.stat().st_size
        else:
            total = 0
            for item in path.rglob('*'):
                if item.is_file():
                    total += item.stat().st_size
            return total
        
        def create_backup(self, source_path: str, backup_name: str = None, compress: bool = True):
        """Create a backup of source path"""
        source = Path(source_path)
        
        if not source.exists():
            self.logger.error(f"Source path {source_path} does not exist")
            return None
        
        # Generate backup name
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        if not backup_name:
            backup_name = f"{source.name}_{timestamp}"
        
        # Create backup file
        if compress:
            backup_file = self.backup_dir / f"{backup_name}.tar.gz"
            self.logger.info(f"Creating compressed backup: {backup_file}")
            
            with tarfile.open(backup_file, "w:gz") as tar:
                tar.add(source, arcname=source.name)
        else:
            backup_file = self.backup_dir / backup_name
            self.logger.info(f"Creating backup: {backup_file}")
            
            if source.is_file():
                shutil.copy2(source, backup_file)
            else:
                shutil.copytree(source, backup_file)
        
        # Calculate backup info
        backup_size = self._get_file_size(backup_file)
        checksum = self._calculate_checksum(backup_file) if backup_file.is_file() else None
        
        # Add to metadata
        backup_info = {
            'name': backup_name,
            'source': str(source),
            'created_at': timestamp,
            'size': backup_size,
            'checksum': checksum,
            'compressed': compress,
            'path': str(backup_file)
        }
        
        self.metadata['backups'].append(backup_info)
        self.metadata['total_size'] += backup_size
        self._save_metadata()
        
        self.logger.info(f"✅ Backup created successfully: {backup_file}")
        return backup_info