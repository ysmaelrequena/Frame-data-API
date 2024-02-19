from fastapi import FastAPI
from database_queries import character_list

app = FastAPI()

@app.get("/characters")
def characters():
    return character_list()

'''
@app.get("/A.K.I.")
def aki_moveset():
    return 
'''