import sqlite3
import pandas as pd

def connect_to_db(db_path):
    """Establish connection to SQLite database"""
    return sqlite3.connect(db_path)

def list_tables(conn):
    """Get list of all tables in database"""
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    return pd.read_sql_query(query, conn)['name'].tolist()

def get_table_schema(conn, table_name):
    """Get column definitions for a table"""
    query = f"PRAGMA table_info({table_name});"
    return pd.read_sql_query(query, conn)

def get_table_data(conn, table_name):
    """Get all data from a specific table"""
    query = f"SELECT * FROM {table_name};"
    return pd.read_sql_query(query, conn)

def execute_query(conn, query):
    """Execute a SQL query and return results"""
    return pd.read_sql_query(query, conn)
