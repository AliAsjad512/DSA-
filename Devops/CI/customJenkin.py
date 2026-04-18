import jenkins
import yaml
import argparse
import os
from pathlib import Path

class JenkinsJobBuilder:
    def __init__(self, url, username, password):
        self.server = jenkins.Jenkins(url, username=username, password=password)
