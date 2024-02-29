from .character_class import *
import mysql.connector

def create_connection():
    connection_params = {
        'host': '',
        'user': '',
        'password': '',
        'database': 'fighting_game_api'
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
    
