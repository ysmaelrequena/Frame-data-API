import mysql.connector
import json
import asyncio
from db_connection import create_connection, get_cursor
from character_class import Character
#In this module I'll create the characters table, I'm gonna hard code it, since it isn't going to change, and i'll add new characters as they come out

character_framedata = None
normals = {}
command_normals = {}
target_combos = {} 
throws = {}
drive_system = {}
special_moves = {}
super_arts = {}
taunts = {}
serenity_stance = {}


table_names = ['normals', 'command_normals', 'target_combos', 'throws', 'drive_system', 'special_moves', 'super_arts', 'taunts']
dict_names = []

# Create classes for all characters with their basic info to pull the data for the db

async def character_class_definer(character_id):
    
    global name, character_framedata, normals, command_normals, target_combos, throws, drive_system, special_moves, super_arts, taunts, serenity_stance, dict_names
    
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
    normals = character_framedata.get('Normals', 'NULL')
    command_normals = character_framedata.get('Command Normals', 'NULL')
    target_combos = character_framedata.get('Target Combos', 'NULL')
    throws = character_framedata.get('Throws', 'NULL')
    drive_system = character_framedata.get('Drive System', 'NULL')
    special_moves = character_framedata.get('Special Moves', 'NULL')
    super_arts = character_framedata.get('Super Arts', 'Null')
    taunts = character_framedata.get('Taunts', 'NULL')
    serenity_stance = character_framedata.get('Serenity Stream', 'Null')
    dict_names = [normals, command_normals, target_combos, throws, drive_system, special_moves, super_arts, taunts]
    
    
    
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

    #table_reset_query = f'DROP TABLE IF EXISTS {table}'
    
    #cursor.execute(table_reset_query)
  
    # We recreate the table with the same constraints
    
    table_recreation_query = f'''CREATE TABLE IF NOT EXISTS {table} (
            move_id SMALLINT PRIMARY KEY AUTO_INCREMENT UNIQUE,
            character_id INT,
            move_name VARCHAR(60) NOT NULL,
            move_nomenclature VARCHAR(50) NOT NULL,
            startup VARCHAR(255),
            active_f VARCHAR(255),
            recovery VARCHAR(255),
            cancel VARCHAR(25),
            damage VARCHAR(255),
            guard VARCHAR(255),
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
            
    for move_nom, move_info in move_t.items():
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
    if current_character_id <= max_character_id:
        # Ensure completion of asynchronous calls
        await character_class_definer(current_character_id)

        for move_type, table in zip(dict_names,table_names):
            print(table)

            await insert_data_db(move_type, table, current_character_id)

        if current_character_id == 4:
            print('serenity stance')
            await insert_data_db(serenity_stance, 'serenity_stance', current_character_id)

        # Recursive call with proper awaiting
        return await main_data_insert_recursion(current_character_id + 1, max_character_id)
        
asyncio.run(main_data_insert_recursion(1, 20))

    


    
