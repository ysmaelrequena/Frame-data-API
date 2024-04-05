from fastapi import FastAPI
from routers.SF6 import sf6_endpoints
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from pydantic import BaseModel
#from db_connection_generic import create_connection, get_cursor
import mysql.connector
from routers.auth import auth_router


app = FastAPI()

# Routers

@app.get("/")

def welcome():
    return '''Welcome to the Fighting Game API! Please visit our documentation: (GH documentation) or url/docs for information about the endpoints of the API.'''

app.include_router(sf6_endpoints.sf6_router)
app.include_router(auth_router.security_router)