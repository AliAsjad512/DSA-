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
        

        def get_connection_stats(self):
        """Get current connection count"""
        cursor = self.conn.cursor()
        if self.db_type == 'postgres':
            cursor.execute("SELECT count(*) FROM pg_stat_activity")
        else:
            cursor.execute("SHOW STATUS LIKE 'Threads_connected'")
        return cursor.fetchone()[0]

    def get_database_size(self):
        """Get database size"""
        cursor = self.conn.cursor()
        if self.db_type == 'postgres':
            cursor.execute("SELECT pg_database_size(current_database())")
            return cursor.fetchone()[0] / (1024**3)  # GB
        else:
            cursor.execute("SELECT SUM(data_length + index_length) FROM information_schema.tables WHERE table_schema = DATABASE()")
            return cursor.fetchone()[0] / (1024**3) if cursor.fetchone()[0] else 0

    def monitor_loop(self, interval=60, slow_threshold=1):
        """Continuous monitoring"""
        self.logger.info(f"Starting DB monitor for {self.db_type}, interval={interval}s")
        while True:
            try:
                slow_queries = self.get_slow_queries_postgres(threshold_seconds=slow_threshold) if self.db_type == 'postgres' else self.get_slow_queries_mysql(slow_threshold)
                conn_count = self.get_connection_stats()
                db_size = self.get_database_size()
                self.logger.info(f"Connections: {conn_count}, DB Size: {db_size:.2f} GB, Slow queries: {len(slow_queries)}")
                if slow_queries:
                    self.logger.warning(f"Slow queries found: {slow_queries[:3]}")
                time.sleep(interval)
            except KeyboardInterrupt:
                break
            except Exception as e:
                self.logger.error(f"Monitor error: {e}")
                time.sleep(interval)
