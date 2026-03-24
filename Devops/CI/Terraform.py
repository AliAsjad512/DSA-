#!/usr/bin/env python3
#Terraform State Manager - Backup, lock, and manage Terraform state files


import os
import boto3
import json
import argparse
import time
from datetime import datetime