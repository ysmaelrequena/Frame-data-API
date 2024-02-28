from fastapi import FastAPI
from database_queries import character_list
from database_queries import character_moveset_fetch
from database_queries import retrieve_id

app = FastAPI()

#Endpoint for the character list

@app.get("/characters/")
def characters():
    return character_list()

#Endpoint for A.K.I.

@app.get("/characters/a.k.i")
def aki_moveset():
    return character_moveset_fetch(1, 'A.K.I.')

#Endpoint for Blanka

@app.get("/characters/blanka")
def blanka_moveset():
    return character_moveset_fetch(2, 'Blanka')

#Endpoint for Cammy

@app.get("/characters/cammy")
def cammy_moveset():
    return character_moveset_fetch(3, 'Cammy')

#Endpoint for Chun-Li

@app.get("/characters/chun-li")
def chunli_moveset():
    return character_moveset_fetch(4, 'Chun-Li')

#Endpoint for Dee-Jay

@app.get("/characters/dee_jay")
def deejay_moveset():
    return character_moveset_fetch(5, 'Dee Jay')

#Endpoint for Dhalsim

@app.get("/characters/dhalsim")
def dhalsim_moveset():
    return character_moveset_fetch(6, 'Dhalsim')

#Endpoint for Ed

@app.get("/characters/ed")
def ed_moveset():
    return character_moveset_fetch(7, 'Ed')


#Endpoint for E. Honda

@app.get("/characters/honda")
def honda_moveset():
    return character_moveset_fetch(8, 'E. Honda')

#Endpoint for Guile

@app.get("/characters/guile")
def guile_moveset():
    return character_moveset_fetch(9, 'Guile')

#Endpoint for J.P.

@app.get("/characters/jp")
def jp_moveset():
    return character_moveset_fetch(10, 'J.P.')

#Endpoint for Jamie

@app.get("/characters/jamie")
def jamie_moveset():
    return character_moveset_fetch(11, 'Jamie')

#Endpoint for Juri

@app.get("/characters/juri")
def juri_moveset():
    return character_moveset_fetch(12, 'juri')

#Endpoint for Ken

@app.get("/characters/ken")
def ken_moveset():
    return character_moveset_fetch(13, 'Ken')

#Endpoint for Kimberly

@app.get("/characters/kimberly")
def kimberly_moveset():
    return character_moveset_fetch(14, 'Kimberly')

#Endpoint for Lily

@app.get("/characters/Lily")
def lily_moveset():
    return character_moveset_fetch(15, 'Lily')

#Endpoint for Luke

@app.get("/characters/luke")
def luke_moveset():
    return character_moveset_fetch(16, 'Luke')

#Endpoint for Manon

@app.get("/characters/manon")
def manon_moveset():
    return character_moveset_fetch(17, 'Manon')

#Endpoint for Marisa

@app.get("/characters/marisa")
def marisa_moveset():
    return character_moveset_fetch(18, 'Marisa')

#Endpoint for Rashid

@app.get("/characters/rashid")
def rashid_moveset():
    return character_moveset_fetch(19, 'Rashid')

#Endpoint for Ryu

@app.get("/characters/ryu")
def ryu_moveset():
    return character_moveset_fetch(20, 'Ryu')

#Endpoint for Zangief

@app.get("/characters/zangief")
def zangief_moveset():
    return character_moveset_fetch(21, 'Zangief')



#Endpoint for move display based on type

@app.get("/characters/{character_name}/normals")

def normal_display(character_name: str):
    
    character = character_name.upper()
    
    if character_name == 'dee_jay':
        character = 'DEE JAY'
    
    try:
        id_character = retrieve_id(character)
        print(id_character)
        data = character_moveset_fetch(id_character, character_name)
        print(data)
        return data.get("normals", {"error": "Normals not found for this character"})
    except Exception as err:
        print(f"Error: {err}")
        
@app.get("/characters/{character_name}/command_normals")

def command_normals_display(character_name: str):
    
    character = character_name.upper()
    
    if character_name == 'dee_jay':
        character = 'DEE JAY'
    
    try:
        id_character = retrieve_id(character)
        print(id_character)
        data = character_moveset_fetch(id_character, character_name)
        print(data)
        return data.get("command_normals", {"error": "Command Normals not found for this character"})
    except Exception as err:
        print(f"Error: {err}")
        
@app.get("/characters/{character_name}/target_combos")

def target_combos_display(character_name: str):
    
    character = character_name.upper()
    
    if character_name == 'dee_jay':
        character = 'DEE JAY'
    
    try:
        id_character = retrieve_id(character)
        print(id_character)
        data = character_moveset_fetch(id_character, character_name)
        print(data)
        return data.get("target_combos", {"error": "Target Combos not found for this character"})
    except Exception as err:
        print(f"Error: {err}")
        
@app.get("/characters/{character_name}/throws")

def throws_display(character_name: str):
    
    character = character_name.upper()
    
    if character_name == 'dee_jay':
        character = 'DEE JAY'
    
    try:
        id_character = retrieve_id(character)
        print(id_character)
        data = character_moveset_fetch(id_character, character_name)
        print(data)
        return data.get("throws", {"error": "Throws not found for this character"})
    except Exception as err:
        print(f"Error: {err}")
        
@app.get("/characters/{character_name}/drive_system")

def drive_system_display(character_name: str):
    
    character = character_name.upper()
    
    if character_name == 'dee_jay':
        character = 'DEE JAY'
    
    try:
        id_character = retrieve_id(character)
        print(id_character)
        data = character_moveset_fetch(id_character, character_name)
        print(data)
        return data.get("drive_system", {"drive_system": "Normals not found for this character"})
    except Exception as err:
        print(f"Error: {err}")
        
@app.get("/characters/{character_name}/special_moves")

def special_moves_display(character_name: str):
    
    character = character_name.upper()
    
    if character_name == 'dee_jay':
        character = 'DEE JAY'
    
    try:
        id_character = retrieve_id(character)
        print(id_character)
        data = character_moveset_fetch(id_character, character_name)
        print(data)
        return data.get("special_moves", {"error": "Special Moves not found for this character"})
    except Exception as err:
        print(f"Error: {err}")
        
@app.get("/characters/{character_name}/super_arts")

def super_arts_display(character_name: str):
    
    character = character_name.upper()
    
    if character_name == 'dee_jay':
        character = 'DEE JAY'
    
    try:
        id_character = retrieve_id(character)
        print(id_character)
        data = character_moveset_fetch(id_character, character_name)
        print(data)
        return data.get("super_arts", {"error": "Super Arts not found for this character"})
    except Exception as err:
        print(f"Error: {err}")

@app.get("/characters/{character_name}/taunts")

def taunts_display(character_name: str):
    
    character = character_name.upper()
    
    if character_name == 'dee_jay':
        character = 'DEE JAY'
    
    try:
        id_character = retrieve_id(character)
        print(id_character)
        data = character_moveset_fetch(id_character, character_name)
        print(data)
        return data.get("taunts", {"error": "Taunts not found for this character"})
    except Exception as err:
        print(f"Error: {err}")
        
@app.get("/characters/chun-li/serenity_stream")

def serenity_stream_display():
    
        try:
            data = character_moveset_fetch(4, 'Chun-Li')
            return data.get("serenity_stance", {"error": "Only Chun-Li has Serenity Stream"})
        except Exception as err:
            print(f"Error: {err}")
            

        
    

















