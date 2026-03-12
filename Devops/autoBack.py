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
    
    def list_backups(self):
        """List all backups"""
        if not self.metadata['backups']:
            print("📂 No backups found")
            return
        
        print("\n📋 BACKUP LIST:")
        print("=" * 80)
        print(f"{'Name':<30} {'Date':<20} {'Size':<15} {'Type':<10}")
        print("-" * 80)
        
        for backup in sorted(self.metadata['backups'], key=lambda x: x['created_at'], reverse=True):
            size_mb = backup['size'] / (1024 * 1024)
            backup_type = "Compressed" if backup.get('compressed') else "Directory"
            print(f"{backup['name'][:30]:<30} {backup['created_at']:<20} {size_mb:.2f} MB:{size_mb:<15.2f} MB {backup_type:<10}")
    def restore_backup(self, backup_name: str, destination: str):
        """Restore a backup to destination"""
        # Find backup in metadata
        backup_info = None
        for backup in self.metadata['backups']:
            if backup['name'] == backup_name or backup['path'] == backup_name:
                backup_info = backup
                break
        
        if not backup_info:
            self.logger.error(f"Backup '{backup_name}' not found")
            return False
        
        backup_path = Path(backup_info['path'])
        dest_path = Path(destination)
        
        if not backup_path.exists():
            self.logger.error(f"Backup file {backup_path} does not exist")
            return False
        
        # Verify checksum
        if backup_info.get('checksum'):
            current_checksum = self._calculate_checksum(backup_path)
            if current_checksum != backup_info['checksum']:
                self.logger.warning("⚠️  Checksum mismatch! Backup may be corrupted.")
                response = input("Continue anyway? (y/n): ")
                if response.lower() != 'y':
                    return False
        
        # Create destination directory
        dest_path.mkdir(parents=True, exist_ok=True)
        
        try:
            # Extract based on backup type
            if backup_info.get('compressed'):
                self.logger.info(f"Extracting {backup_path} to {dest_path}")
                with tarfile.open(backup_path, "r:gz") as tar:
                    tar.extractall(dest_path)
            else:
                self.logger.info(f"Copying {backup_path} to {dest_path}")
                if backup_path.is_file():
                    shutil.copy2(backup_path, dest_path)
                else:
                    shutil.copytree(backup_path, dest_path / backup_path.name, dirs_exist_ok=True)
            
            self.logger.info(f"✅ Backup restored successfully to {dest_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to restore backup: {e}")
            return False

            def cleanup_old_backups(self):
        """Remove backups older than retention days"""
        cutoff_date = datetime.now() - timedelta(days=self.retention_days)
        cutoff_str = cutoff_date.strftime('%Y%m%d')
        
        removed = []
        kept = []
        
        for backup in self.metadata['backups'][:]:
            backup_date = backup['created_at'][:8]  # YYYYMMDD
            
            if backup_date < cutoff_str:
                backup_path = Path(backup['path'])
                if backup_path.exists():
                    if backup_path.is_file():
                        backup_path.unlink()
                    else:
                        shutil.rmtree(backup_path)
                    
                    self.metadata['total_size'] -= backup['size']
                    self.metadata['backups'].remove(backup)
                    removed.append(backup['name'])
                else:
                    self.metadata['backups'].remove(backup)
            else:
                kept.append(backup['name'])
        
        self._save_metadata()
        
        self.logger.info(f"🧹 Cleanup completed: Removed {len(removed)} old backups, kept {len(kept)}")
        return removed
    
    def get_backup_stats(self):
        """Get backup statistics"""
        total_backups = len(self.metadata['backups'])
        total_size_gb = self.metadata['total_size'] / (1024**3)
        
        # Group by date
        by_date = {}
        for backup in self.metadata['backups']:
            date = backup['created_at'][:8]  # YYYYMMDD
            by_date[date] = by_date.get(date, 0) + 1
        
        return {
            'total_backups': total_backups,
            'total_size_gb': round(total_size_gb, 2),
            'backups_by_date': by_date,
            'oldest_backup': min(backup['created_at'] for backup in self.metadata['backups']) if self.metadata['backups'] else None,
            'newest_backup': max(backup['created_at'] for backup in self.metadata['backups']) if self.metadata['backups'] else None
        }


    