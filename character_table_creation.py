import mysql.connector
import json
import asyncio
from db_connection import create_connection, get_cursor
from character_class import Character
#In this module I'll create the characters table, I'm gonna hard code it, since it isn't going to change, and i'll add new characters as they come out

character_framedata = None

table_names = ['normals', 'command_normals', 'target_combos', 'throws', 'drive_system', 'special_moves', 'super_arts', 'taunts', 'serenity_stance']


# Create classes for all characters with their basic info to pull the data for the db

async def character_class_definer(character_id):
    
    global name, character_framedata
    
    try:
        connection = create_connection()
        cursor = get_cursor(connection)
    except mysql.connector.Error as err:
                print(f"Error: {err}")
    
    select_query =  f'''
    SELECT character_name FROM characters
    WHERE id = {character_id}
    '''
    
    cursor.execute(select_query)
    result = cursor.fetchone()
    
    if result:
        extracted_name = result[0]
        name = extracted_name.capitalize()
        
        if name == 'Chun-li':
            url = f'''https://wiki.supercombo.gg/w/Street_Fighter_6/Chun-Li'''
        elif name == 'Dee-jay':
            url = f'''https://wiki.supercombo.gg/w/Street_Fighter_6/Dee_Jay'''
        elif name == 'E. honda':
            url = f'''https://wiki.supercombo.gg/w/Street_Fighter_6/E.Honda'''
        elif name == 'J.p':
            url =f'''https://wiki.supercombo.gg/w/Street_Fighter_6/JP'''
        elif name == 'A.k.i':
            url = f'''https://wiki.supercombo.gg/w/Street_Fighter_6/A.K.I.'''
        else:
            url = f'''https://wiki.supercombo.gg/w/Street_Fighter_6/{name}'''
            
        print(url)
        
    else:
        print('none')
        
    cursor.close()
    connection.close()
    
    new_character = Character(name= name, url= url)
    character_framedata = await new_character.get_framedata()
    
    #print(character_framedata.items())
    
# ///////////////////

# Functions for data insertion into the db

async def insert_data_db(move_t, table, character_id):
    
    # We create the connection to the db, based on the parameters imported from the 'db_connection.py' module
    #print(move)
    try:
        connection = create_connection()
        cursor = get_cursor(connection)
    except mysql.connector.Error as err:
                print(f"Error: {err}")
        
    # We reset the table to prevent conflicts with the moves' ID
    ''' 
    table_reset_query = fDROP TABLE IF EXISTS {table}
    
    cursor.execute(table_reset_query)
    '''
    # We recreate the table with the same constraints
    
    table_recreation_query = f'''CREATE TABLE IF NOT EXISTS {table} (
            move_id INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
            character_id INT,
            move_name VARCHAR(60) NOT NULL,
            move_nomenclature VARCHAR(15) NOT NULL,
            startup VARCHAR(255),
            active_f VARCHAR(255),
            recovery VARCHAR(255),
            cancel VARCHAR(25),
            damage VARCHAR(255),
            guard VARCHAR(5),
            on_hit VARCHAR(255),
            on_block VARCHAR(255),
            FOREIGN KEY (character_id) REFERENCES characters(id)
            );
    '''
    
    cursor.execute(table_recreation_query)
    
    #  Then we create the insert query for the information we're passing to our db from our imported class from the module 'character_class.py'
    insert_query = f'''INSERT INTO {table} (character_id, move_name, move_nomenclature, startup, active_f, recovery, cancel, damage, guard, on_hit, on_block)
    
            VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            '''
    for move_type, move in character_framedata.items():
        for move_nom, move_info in move.items():
            for move_name, details in move_info.items():
            
                startup = details.get('Startup', 'NULL')
                active_f = details.get('Active', 'NULL')
                recovery = details.get('Recovery', 'NULL')
                cancel = details.get('Cancel', 'NULL')
                damage = details.get('Damage', 'NULL')
                guard = details.get('Guard', 'NULL')
                on_hit = details.get('On Hit', 'NULL')
                on_block = details.get('On Block', 'NULL')
            
                data = (character_id, move_name, move_nom, startup, active_f, recovery, cancel, damage, guard, on_hit, on_block)
            
                try:
                    cursor.execute(insert_query, data)
                    connection.commit()
                    print('Query executed successfully')
            
                except mysql.connector.Error as err:
                    print(f"Error: {err}")
                
    cursor.close()
    connection.close()
    
async def main_data_insert_recursion(current_character_id, max_character_id):
   
    if current_character_id > max_character_id:
        return

    # Ensure completion of asynchronous calls
    
    await asyncio.gather(character_class_definer(current_character_id))

# tienes que buscar como pasar el dict que necvesitas exactamente a la segunda funcion en cada instancia del loop para que pueda insertar solo esa info en la tabla
#correspondiente, luego, tienes que ajustar el loop de la segunda funcion para solo usar esa data y esa tabla
    for table in table_names:
        print(table)
        
        if table == 'serenity_stance' and name != 'Chun-li':
            continue

        await asyncio.gather(insert_data_db(, table, current_character_id))

    await main_data_insert_recursion(current_character_id + 1, max_character_id)

asyncio.run(main_data_insert_recursion(1, 20))

    


    
