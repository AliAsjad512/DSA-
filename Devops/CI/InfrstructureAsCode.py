import subprocess
import json
import argparse
import sys
import os
from pathlib import Path

class IaCValidator:
    def __init__(self, template_path):
        self.template_path = Path(template_path)