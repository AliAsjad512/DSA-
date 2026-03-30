import boto3
import os
import argparse
import datetime
import gzip
import shutil
import hashlib
import logging
from pathlib import Path

class AWSCostOptimizer: