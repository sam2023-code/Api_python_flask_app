import psycopg2
from psycopg2 import sql

# Database connection configuration
DB_HOST = 'database-1.ce9ca6cwmebj.us-east-1.rds.amazonaws.com'
DB_PORT = '5432'
DB_NAME = 'postgre_aws'
DB_USER = 'postgres'  # replace with your PostgreSQL username
DB_PASS = 'postgres_pass'    # replace with your PostgreSQL password

# Connect to PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn
    