from routers.SF6.db_connection_prod import create_connection, get_cursor
import mysql.connector


#Character list return

def character_list():
    
    characters = {}
    
    try:
        connection = create_connection()
        cursor = get_cursor(connection)
    except mysql.connector.Error as err:
                print(f"Error: {err}")
    
    characters_display_query = f'''
    SELECT * FROM characters
    '''
    
    cursor.execute(characters_display_query)
    rows = cursor.fetchmany(size=23)   

    for char_id, name in rows:
        characters[char_id] = name
    
    
    
    return characters


#character moveset return with frame data response

tables = ['normals', 'command_normals', 'target_combos', 'throws', 'drive_system', 'special_moves', 'super_arts', 'taunts', 'serenity_stance']

def character_moveset_fetch(id: int, name: str):
    
#First, we create the dictionaries that are going to receive the info from the database
    
    if name != 'Chun-Li':
    
        character_moveset = {
                            'character': f'{name}',
                            'id': f'{id}',
                            'normals': {},
                            'command_normals': {},
                            'target_combos': {},
                            'throws': {},
                            'drive_system': {},
                            'special_moves': {},
                            'super_arts': {},
                            'taunts': {}
                            }
    else:
        
        character_moveset = {
                            'character': f'{name}',
                            'id': f'{id}',
                            'normals': {},
                            'command_normals': {},
                            'target_combos': {},
                            'throws': {},
                            'drive_system': {},
                            'special_moves': {},
                            'super_arts': {},
                            'taunts': {},
                            'serenity_stance': {}
                            }
        

#Then, we connect to the db to retrieve the info.

    try:
        
        connection = create_connection()
        cursor = get_cursor(connection)
        
        subdict_name = ''
        
        
        for move_type in tables:
            character_moveset_fetch = f'''
                SELECT move_name, move_nomenclature, startup, active_f, recovery, cancel, damage, guard, on_hit, on_block FROM {move_type}
                WHERE character_id = {id};
                '''
            cursor.execute(character_moveset_fetch)
            moveset = cursor.fetchall()

            for move_nomenclature, move_name, startup, active_f, recovery, cancel, damage, guard, on_hit, on_block in moveset:               

                # Update the character_moveset with the inner moveset
                character_moveset.setdefault(move_type, {})['_'.join(move_name.split(' '))] = {
                    'move_name': move_name,
                    'nomenclature': move_nomenclature,
                    'startup': startup,
                    'active_f': active_f,
                    'recovery': recovery,
                    'cancel': cancel,
                    'damage': damage,
                    'guard': guard,
                    'on_hit': on_hit,
                    'on_block': on_block
                }
                
        connection.close()
        cursor.close()

        return character_moveset
                
            
    except mysql.connector.Error as err:
                print(f"Error: {err}")
                

                

#function to retrieve the id of characters for the queries for just a single type of move

def retrieve_id(name: str):
    
    try:
        
        connection = create_connection()
        cursor = get_cursor(connection)
        
        id_query = f'''
        SELECT id from characters
        WHERE character_name = '{name.upper()}';
        '''
    
        cursor.execute(id_query)
        id_char = cursor.fetchone()
        
        cursor.close()
        connection.close() 
        
        return id_char[0] 
        
    except mysql.connector.Error as err:
                print(f"Error: {err}")    
                

            
        
        
        
                
    

    
    
    
    
    
    