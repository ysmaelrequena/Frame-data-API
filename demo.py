from fastapi import FastAPI
from routers.SF6 import sf6_endpoints
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from pydantic import BaseModel
#from db_connection_generic import create_connection, get_cursor
import mysql.connector


app = FastAPI()

# Routers

@app.get("/")

def welcome():
    return '''Welcome to the Fighting Game API! Please visit our documentation: (GH documentation) or url/docs for information about the endpoints of the API.'''

def health_check():
    return {"status": "healthy"}

app.include_router(sf6_endpoints.sf6_router)