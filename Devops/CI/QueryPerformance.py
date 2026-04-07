import psycopg2
import pymysql
import time
import json
import argparse
import logging
from datetime import datetime, timedelta
import subprocess

   class DBMonitor:
    def __init__(self, db_type, host, port, user, password, database):
        self.db_type = db_type
        self.conn = self._connect(host, port, user, password, database)
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def _connect(self, host, port, user, password, database):
        if self.db_type == 'postgres':
            return psycopg2.connect(host=host, port=port, user=user, password=password, database=database)
        elif self.db_type == 'mysql':
            return pymysql.connect(host=host, port=port, user=user, password=password, database=database)
        else:
            raise ValueError(f"Unsupported db_type: {self.db_type}")