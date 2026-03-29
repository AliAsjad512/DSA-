import subprocess
import json
import argparse
import sys
import os

class DockerImageScanner:
    def __init__(self, image_name):
        self.image_name = image_name