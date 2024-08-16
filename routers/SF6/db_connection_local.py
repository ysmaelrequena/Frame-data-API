from routers.SF6.character_class import *
import mysql.connector
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

db_host=os.getenv("LOCALDB_HOST")
user_db=os.getenv("LOCALDB_USER")
fdapi_pass=os.getenv("DB_KEY")

def create_connection():
    connection_params = {
        'host': db_host,
        'user': user_db,
        'password': fdapi_pass,
        'database': 'frame_data_api'
    }
    
    try:
        connection = mysql.connector.connect(**connection_params)
        return connection
    except Exception as e:
        print(f"Error: Unable to connect to the database - {e}")
        raise

def get_cursor(connection):
    try:
        cursor = connection.cursor()
        return cursor
    except Exception as e:
        print(f"Error: Unable to create a database cursor - {e}")
        raise
    
def get_cursor_dict(connection):
    try:
        cursor = connection.cursor(dictionary=True)
        return cursor
    except Exception as e:
        print(f"Error: Unable to create a database cursor - {e}")
        raise
    
def create_connection_users():
    connection_params = {
        'host': 'fdapi_users_db',
        'user': 'root',
        'password': 'yjro24766337',
        'database': 'users_FDAPI'
    }
    
    try:
        connection = mysql.connector.connect(**connection_params)
        return connection
    except Exception as e:
        print(f"Error: Unable to connect to the database - {e}")
        raise
    
