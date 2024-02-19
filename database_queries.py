from db_connection import create_connection, get_cursor
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
    rows = cursor.fetchmany(size=20)   

    for char_id, name in rows:
        characters[char_id] = name 
    
    return characters


#character moveset return with frame data response

def character_moveset_fetch(id: int, name: str, table: str):
    
    try:
        connection = create_connection()
        cursor = get_cursor(connection)
    except mysql.connector.Error as err:
                print(f"Error: {err}")
                
    normals_fetch_query = f'''
    SELECT move_name, move_nomenclature, startup, active_f, recovery, cancel, damage, guard, on_hit, on_block FROM normals
    WHERE character_id = {id};
    '''
    
    specials_fetch_query = f'''
    SELECT move_name, move_nomenclature, startup, active_f, recovery, cancel, damage, guard, on_hit, on_block FROM special_moves
    WHERE character_id = {id};
    '''
    
    cmd_normals_fetch_query = f'''
    SELECT move_name, move_nomenclature, startup, active_f, recovery, cancel, damage, guard, on_hit, on_block FROM command_normals
    WHERE character_id = {id};
    '''
    
    tgt_combos_fetch_query = f'''
    SELECT move_name, move_nomenclature, startup, active_f, recovery, cancel, damage, guard, on_hit, on_block FROM target_combos
    WHERE character_id = {id};
    '''
    
    throws_fetch_query = f'''
    SELECT move_name, move_nomenclature, startup, active_f, recovery, cancel, damage, guard, on_hit, on_block FROM throws
    WHERE character_id = {id};
    '''
    
    drv_system_fetch_query = f'''
    SELECT move_name, move_nomenclature, startup, active_f, recovery, cancel, damage, guard, on_hit, on_block FROM drive_system
    WHERE character_id = {id};
    '''
    
    special_moves_fetch_query = f'''
    SELECT move_name, move_nomenclature, startup, active_f, recovery, cancel, damage, guard, on_hit, on_block FROM target_combos
    WHERE character_id = {id};
    '''


    
    
    
    
    
    