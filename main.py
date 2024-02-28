from fastapi import FastAPI
from database_queries import character_list
from database_queries import character_moveset_fetch

app = FastAPI()

#Endpoint for the character list

@app.get("/characters")
def characters():
    return character_list()

#Endpoint for A.K.I.

@app.get("/a.k.i")
def aki_moveset():
    return character_moveset_fetch(1, 'A.K.I.')

#Endpoint for Blanka

@app.get("/blanka")
def blanka_moveset():
    return character_moveset_fetch(2, 'Blanka')

#Endpoint for Cammy

@app.get("/cammy")
def cammy_moveset():
    return character_moveset_fetch(3, 'Cammy')

#Endpoint for Chun-Li

@app.get("/chunli")
def chunli_moveset():
    return character_moveset_fetch(4, 'Chun-Li')

#Endpoint for Dee-Jay

@app.get("/deejay")
def deejay_moveset():
    return character_moveset_fetch(5, 'Dee Jay')

#Endpoint for Dhalsim

@app.get("/dhalsim")
def dhalsim_moveset():
    return character_moveset_fetch(6, 'Dhalsim')

#Endpoint for Ed

@app.get("/ed")
def ed_moveset():
    return character_moveset_fetch(7, 'Ed')


#Endpoint for E. Honda

@app.get("/honda")
def honda_moveset():
    return character_moveset_fetch(8, 'E. Honda')

#Endpoint for Guile

@app.get("/guile")
def guile_moveset():
    return character_moveset_fetch(9, 'Guile')

#Endpoint for J.P.

@app.get("/jp")
def jp_moveset():
    return character_moveset_fetch(10, 'J.P.')

#Endpoint for Jamie

@app.get("/jamie")
def jamie_moveset():
    return character_moveset_fetch(11, 'Jamie')

#Endpoint for Juri

@app.get("/juri")
def juri_moveset():
    return character_moveset_fetch(12, 'juri')

#Endpoint for Ken

@app.get("/ken")
def ken_moveset():
    return character_moveset_fetch(13, 'Ken')

#Endpoint for Kimberly

@app.get("/kimberly")
def kimberly_moveset():
    return character_moveset_fetch(14, 'Kimberly')

#Endpoint for Lily

@app.get("/Lily")
def lily_moveset():
    return character_moveset_fetch(15, 'Lily')

#Endpoint for Luke

@app.get("/luke")
def luke_moveset():
    return character_moveset_fetch(16, 'Luke')

#Endpoint for Manon

@app.get("/manon")
def manon_moveset():
    return character_moveset_fetch(17, 'Manon')

#Endpoint for Marisa

@app.get("/marisa")
def marisa_moveset():
    return character_moveset_fetch(18, 'Marisa')

#Endpoint for Rashid

@app.get("/rashid")
def rashid_moveset():
    return character_moveset_fetch(19, 'Rashid')

#Endpoint for Ryu

@app.get("/ryu")
def ryu_moveset():
    return character_moveset_fetch(20, 'Ryu')

#Endpoint for Zangief

@app.get("/zangief")
def zangief_moveset():
    return character_moveset_fetch(21, 'Zangief')

















