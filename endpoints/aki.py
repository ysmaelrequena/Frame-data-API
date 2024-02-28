from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector


def process_request():
    
    try:
        connection = create_connection()
        cursor = get_cursor(connection)
    except mysql.connector.Error as err:
                print(f"Error: {err}")
                
    move_selection_query = f'''
    SELECT * FROM normals
    WHERE character_id == 1
    ORDER BY 
    '''
    
    cursor.execute(move_selection_query)
    rows = cursor.fetchmany(size=5)
    
    for row in rows:
        print(row)
        
process_request()