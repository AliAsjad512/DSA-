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