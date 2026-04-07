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
        

         def get_slow_queries_postgres(self, threshold_seconds=1):
        """Get slow queries from PostgreSQL pg_stat_statements"""
        cursor = self.conn.cursor()
        query = """
        SELECT query, mean_time, calls, total_time, max_time
        FROM pg_stat_statements
        WHERE mean_time > %s
        ORDER BY mean_time DESC
        LIMIT 10
        """
        cursor.execute(query, (threshold_seconds * 1000,))  # mean_time is in ms
        results = cursor.fetchall()
        return [{'query': r[0][:200], 'mean_time_ms': round(r[1], 2), 'calls': r[2], 'total_time_ms': round(r[3], 2)} for r in results]
def get_slow_queries_mysql(self, threshold_seconds=1):
        """Get slow queries from MySQL slow log (requires slow log enabled)"""
        cursor = self.conn.cursor()
        # Check if slow query log is on
        cursor.execute("SHOW VARIABLES LIKE 'slow_query_log'")
        slow_log_on = cursor.fetchone()
        if slow_log_on and slow_log_on[1] == 'ON':
            cursor.execute(f"SELECT sql_text, query_time, lock_time, rows_examined FROM mysql.slow_log WHERE query_time > {threshold_seconds} ORDER BY query_time DESC LIMIT 10")
            results = cursor.fetchall()
            return [{'query': r[0][:200], 'query_time': float(r[1]), 'lock_time': float(r[2]), 'rows_examined': r[3]} for r in results]
        else:
            return [{'error': 'Slow query log not enabled'}]