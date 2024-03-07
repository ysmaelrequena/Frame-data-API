from fastapi import APIRouter
from routers.SF6.database_queries import character_list
from routers.SF6.database_queries import character_moveset_fetch
from routers.SF6.database_queries import retrieve_id

sf6_router = APIRouter(prefix="/SF6/characters",tags=['sf6'])

#Endpoint for the character list

@sf6_router.get("/")
async def characters():
    return character_list()

#Endpoint for Character movesets.

@sf6_router.get("/{character_name}")
async def character_moves(character_name: str):
    id_char = retrieve_id(character_name)
    return character_moveset_fetch(id_char, f'{character_name}')

#Endpoint for movetype list

@sf6_router.get("/{character_name}/movetype_list_name")
async def movetype_list_name(character_name: str):
    
    list = {}
    id_char = retrieve_id(character_name)
    moveset = character_moveset_fetch(id_char, f'{character_name}')
    del moveset['character']
    del moveset['id']
    
    for count, type in enumerate(moveset.keys()):
        list[count] = type
        
    return list
    

#Endpoint for move display based on type

@sf6_router.get("/{character_name}/{movetype}")

def movetype_display(character_name: str, movetype: str):
    
    character = character_name.upper()
    
    try:
        
        id_character = retrieve_id(character)
        data = character_moveset_fetch(id_character, character_name)
        return data.get(f'{movetype}', {"error": f"{movetype} not found for this character"})
    
    except Exception as err:
        print(f"Error: {err}")
        
'''
Version 2:
Trabajar en endpoint que devuelva al usuario un CSV con la informacion de todos los personajes
'''












