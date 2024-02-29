from fastapi import APIRouter
from .database_queries import character_list
from .database_queries import character_moveset_fetch
from .database_queries import retrieve_id

sf6_router = APIRouter(prefix="/characters")

#Endpoint for the character list

@sf6_router.get("/")
async def characters():
    return character_list()

#Endpoint for A.K.I.

@sf6_router.get("/a.k.i")
async def aki_moveset():
    return character_moveset_fetch(1, 'A.K.I.')

#Endpoint for Blanka

@sf6_router.get("/blanka")
async def blanka_moveset():
    return character_moveset_fetch(2, 'Blanka')

#Endpoint for Cammy

@sf6_router.get("/cammy")
async def cammy_moveset():
    return character_moveset_fetch(3, 'Cammy')

#Endpoint for Chun-Li

@sf6_router.get("/chun-li")
async def chunli_moveset():
    return character_moveset_fetch(4, 'Chun-Li')

#Endpoint for Dee-Jay

@sf6_router.get("/dee_jay")
async def deejay_moveset():
    return character_moveset_fetch(5, 'Dee Jay')

#Endpoint for Dhalsim

@sf6_router.get("/dhalsim")
async def dhalsim_moveset():
    return character_moveset_fetch(6, 'Dhalsim')

#Endpoint for Ed

@sf6_router.get("/ed")
async def ed_moveset():
    return character_moveset_fetch(7, 'Ed')


#Endpoint for E. Honda

@sf6_router.get("/honda")
async def honda_moveset():
    return character_moveset_fetch(8, 'E. Honda')

#Endpoint for Guile

@sf6_router.get("/guile")
async def guile_moveset():
    return character_moveset_fetch(9, 'Guile')

#Endpoint for J.P.

@sf6_router.get("/jp")
async def jp_moveset():
    return character_moveset_fetch(10, 'J.P.')

#Endpoint for Jamie

@sf6_router.get("/jamie")
async def jamie_moveset():
    return character_moveset_fetch(11, 'Jamie')

#Endpoint for Juri

@sf6_router.get("/juri")
async def juri_moveset():
    return character_moveset_fetch(12, 'juri')

#Endpoint for Ken

@sf6_router.get("/ken")
async def ken_moveset():
    return character_moveset_fetch(13, 'Ken')

#Endpoint for Kimberly

@sf6_router.get("/kimberly")
async def kimberly_moveset():
    return character_moveset_fetch(14, 'Kimberly')

#Endpoint for Lily

@sf6_router.get("/Lily")
async def lily_moveset():
    return character_moveset_fetch(15, 'Lily')

#Endpoint for Luke

@sf6_router.get("/luke")
async def luke_moveset():
    return character_moveset_fetch(16, 'Luke')

#Endpoint for Manon

@sf6_router.get("/manon")
async def manon_moveset():
    return character_moveset_fetch(17, 'Manon')

#Endpoint for Marisa

@sf6_router.get("/marisa")
async def marisa_moveset():
    return character_moveset_fetch(18, 'Marisa')

#Endpoint for Rashid

@sf6_router.get("/rashid")
async def rashid_moveset():
    return character_moveset_fetch(19, 'Rashid')

#Endpoint for Ryu

@sf6_router.get("/ryu")
async def ryu_moveset():
    return character_moveset_fetch(20, 'Ryu')

#Endpoint for Zangief

@sf6_router.get("/zangief")
async def zangief_moveset():
    return character_moveset_fetch(21, 'Zangief')



#Endpoint for move display based on type

'''
#Work in progress to just simplify the GET requests by movetype
@app.get("/characters/{character_name}/{movetype}")

'''

@sf6_router.get("/{character_name}/normals")

def normal_display(character_name: str):
    
    character = character_name.upper()
    
    if character_name == 'dee_jay':
        character = 'DEE JAY'
    
    try:
        id_character = retrieve_id(character)
        data = character_moveset_fetch(id_character, character_name)
        return data.get("normals", {"error": "Normals not found for this character"})
    except Exception as err:
        print(f"Error: {err}")
        
@sf6_router.get("/{character_name}/command_normals")

def command_normals_display(character_name: str):
    
    character = character_name.upper()
    
    if character_name == 'dee_jay':
        character = 'DEE JAY'
    
    try:
        id_character = retrieve_id(character)
        data = character_moveset_fetch(id_character, character_name)
        return data.get("command_normals", {"error": "Command Normals not found for this character"})
    except Exception as err:
        print(f"Error: {err}")
        
@sf6_router.get("/{character_name}/target_combos")

def target_combos_display(character_name: str):
    
    character = character_name.upper()
    
    if character_name == 'dee_jay':
        character = 'DEE JAY'
    
    try:
        id_character = retrieve_id(character)
        data = character_moveset_fetch(id_character, character_name)
        return data.get("target_combos", {"error": "Target Combos not found for this character"})
    except Exception as err:
        print(f"Error: {err}")
        
@sf6_router.get("/{character_name}/throws")

def throws_display(character_name: str):
    
    character = character_name.upper()
    
    if character_name == 'dee_jay':
        character = 'DEE JAY'
    
    try:
        id_character = retrieve_id(character)
        data = character_moveset_fetch(id_character, character_name)
        return data.get("throws", {"error": "Throws not found for this character"})
    except Exception as err:
        print(f"Error: {err}")
        
@sf6_router.get("/{character_name}/drive_system")

def drive_system_display(character_name: str):
    
    character = character_name.upper()
    
    if character_name == 'dee_jay':
        character = 'DEE JAY'
    
    try:
        id_character = retrieve_id(character)
        data = character_moveset_fetch(id_character, character_name)
        return data.get("drive_system", {"drive_system": "Normals not found for this character"})
    except Exception as err:
        print(f"Error: {err}")
        
@sf6_router.get("/{character_name}/special_moves")

def special_moves_display(character_name: str):
    
    character = character_name.upper()
    
    if character_name == 'dee_jay':
        character = 'DEE JAY'
    
    try:
        id_character = retrieve_id(character)
        data = character_moveset_fetch(id_character, character_name)
        print(data.get("special_moves"))
        return data.get("special_moves", {"error": "Special Moves not found for this character"})
    except Exception as err:
        print(f"Error: {err}")
        
@sf6_router.get("/{character_name}/super_arts")

def super_arts_display(character_name: str):
    
    character = character_name.upper()
    
    if character_name == 'dee_jay':
        character = 'DEE JAY'
    
    try:
        id_character = retrieve_id(character)
        data = character_moveset_fetch(id_character, character_name)
        return data.get("super_arts", {"error": "Super Arts not found for this character"})
    except Exception as err:
        print(f"Error: {err}")

@sf6_router.get("/{character_name}/taunts")

def taunts_display(character_name: str):
    
    character = character_name.upper()
    
    if character_name == 'dee_jay':
        character = 'DEE JAY'
    
    try:
        id_character = retrieve_id(character)
        data = character_moveset_fetch(id_character, character_name)
        return data.get("taunts", {"error": "Taunts not found for this character"})
    except Exception as err:
        print(f"Error: {err}")
        
@sf6_router.get("/chun-li/serenity_stream")

def serenity_stream_display():
    
        try:
            data = character_moveset_fetch(4, 'Chun-Li')
            return data.get("serenity_stance", {"error": "Only Chun-Li has Serenity Stream"})
        except Exception as err:
            print(f"Error: {err}")
            

            

        
    

















