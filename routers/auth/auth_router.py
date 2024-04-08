from fastapi import Depends, status, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from .security import Token, TokenData, User, UserInDB, get_user, get_user_for_verification, create_access_token, get_current_user, get_current_active_user,user_verification, ACCESS_TOKEN_EXPIRE_MINUTES

security_router = APIRouter(prefix="/auth")


@security_router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    
    user = user_verification(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'}
        )
        
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data= {'sub': user}, expires_delta=access_token_expires)
    
    return {'access_token': access_token, 'token_type': 'bearer'}

@security_router.get("/users/me", response_model=User)

async def read_my_user(current_user: User = Depends(get_current_active_user)):
    return current_user








        
    
    