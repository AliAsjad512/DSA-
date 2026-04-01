import os
import subprocess
import argparse
import shutil
from pathlib import Path

class GitAutomation:
    def __init__(self, repo_path=None):
        self.repo_path = Path(repo_path) if repo_path else Path.cwd()