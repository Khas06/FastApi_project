from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from . import schemas, database, models
from .config import settings

oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')


SEKRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SEKRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token:str, credentials_exeption):

    try:
        payload = jwt.decode(token, SEKRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")


        if id is None:
            raise credentials_exeption
    
        token_data = schemas.TokenData(id=id)
    
    except JWTError:
        raise credentials_exeption

    return token_data


def get_current_user(token: str = Depends(oauth2_schema), db: Session = Depends(database.get_db)):
    credentials_exeption = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail= "Could not validate credentials",
                                         headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credentials_exeption)
    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user

