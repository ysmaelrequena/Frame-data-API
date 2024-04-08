from fastapi import Depends, status
from pydantic import BaseModel
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from db_connection_generic import create_connection, get_cursor_dict
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
import mysql.connector

SECRET_KEY = '4003c3bff38f3698e5fdc6b384643e4d888b28c7aaac10e3e854a52d564311b3'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 2880

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    user_id: int
    username: str | None = None
    full_name: str | None = None
    email: str | None = None
    disabled: bool | None = None
    
class UserInDB(User):
    hashed_password: str

user_instance = None    
user_in_db_instance = None
    
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

def verify_password(plain_pass, hashed_pass):
    return pwd_context.verify(plain_pass, hashed_pass)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(user: str):
    
    try:
        connection = create_connection()
        cursor = get_cursor_dict(connection)
    
        user_query= """
        SELECT * FROM users
        WHERE username = %s
        """
  
        cursor.execute(user_query, (user,))
        user_dictnp = cursor.fetchone()

        if user_dictnp:
            user_instance = User(**user_dictnp)
            return user_instance
        else:
            return None

    except mysql.connector.Error as err:
                print(f"Error: {err}")
                
    finally:
        cursor.close()
        connection.close()


def get_user_for_verification(user: str):
    
    try:
        connection = create_connection()
        cursor = get_cursor_dict(connection)
    
        userInDB_query = """
        SELECT * FROM users a
        LEFT JOIN user_pass b
        ON a.user_id = b.user_id
        WHERE a.username = %s
        """
        
        cursor.execute(userInDB_query, (user,))
        user_data = cursor.fetchone()

        if user_data:
            user_in_db_instance = UserInDB(**user_data)
            return user_in_db_instance
        else:
            return None

    except mysql.connector.Error as err:
                print(f"Error: {err}")
                
    finally:
        cursor.close()
        connection.close()
        
                
def user_verification(username: str, passw: str):
    
    user_info = get_user_for_verification(username)
    if not user_info:
        raise HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED, 
        detail='The username or password entered are not correct',
        headers={'WWW-Authenticate': 'Bearer'}    
        )
        
    password_verification = verify_password(passw, user_info.hashed_password)
    
    if not password_verification:
        raise HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED, 
        detail='The username or password entered are not correct',
        headers={'WWW-Authenticate': 'Bearer'}    
        )
    
    if password_verification == True:
        return user_info.username
    
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
        
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt
        
           
async def get_current_user(token: str =  Depends(oauth2_scheme)):
    credential_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='Unauthenticated', 
            headers={'WWW-Authenticate': 'Bearer'}
        )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise credential_exception
        token_data = TokenData(username=username)
        
    except JWTError:
        raise credential_exception
    
    user = get_user(token_data.username)
    
    if user is None:
        raise credential_exception
    else:
        return user
    
async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Inactive User'
        )
    
    return current_user

