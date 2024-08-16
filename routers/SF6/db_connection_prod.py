from routers.SF6.character_class import *
import mysql.connector

def create_connection():
    connection_params = {
        'host': 'fdapi-demo.c1mscg0yumsx.us-east-2.rds.amazonaws.com',
        'user': 'admin',
        'password': 'yjro24766337',
        'database': 'frame_data_api'
    }
    
    try:
        connection = mysql.connector.connect(**connection_params)
        return connection
    except Exception as e:
        print(f"Error: Unable to connect to the database - {e}")
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
    
