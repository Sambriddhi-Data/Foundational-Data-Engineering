# Extractor/database_connector.py
'''Database connection module for PostgreSQL using psycopg2 and SQLAlchemy.'''

import psycopg2
from sqlalchemy import create_engine
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseConnector:
    def __init__(self, config):
        self.config = config['database']

# Initialize the database connection
    def get_connection(self):
        return psycopg2.connect(**self.config)

# Get SQLAlchemy engine for ORM operations
    def get_engine(self):
        conn_str = f"postgresql://{self.config['user']}:{self.config['password']}@{self.config['host']}:{self.config['port']}/{self.config['database']}"
        return create_engine(conn_str)
