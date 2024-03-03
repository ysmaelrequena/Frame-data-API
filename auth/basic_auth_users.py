import fastapi
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

class User(BaseModel):
    username: str
    full_name: str
    password: str
    disabled: bool
    
app = fastapi()

oauth = OAuth2PasswordBearer(tokenUrl=)
    

'''def search_user(username:str):
    if username in 
    '''