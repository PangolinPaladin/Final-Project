from fastapi import FastAPI, Depends, HTTPException, status
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer 
from datetime import datetime, timedelta, timezone

from sqlmodel import Session, select
from sqlalchemy.exc import IntegrityError
from db import get_session

from models.urls import Urls
from models.users import User, UserSchema, UserAccountSchema
from models.tokens import Token, BlacklistedToken, create_access_token

import config

from services import get_current_user_token, create_user, get_user 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


app = FastAPI()

origins = [
    "http://localhost:5173",
    ]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/")
async def root():
    return {"message": "Squids Rule"}

@app.get("/urls")
async def get_all_urls(session: Session = Depends(get_session)):
    statement = select(Urls)
    flapjacks = session.exec(statement).all()
    
    return flapjacks 

@app.get("/urls/{id}")
async def get_single_url(id: str, session: Session = Depends(get_session)):
    statement = select(Urls).where(Urls.id == id)
    result = session.exec(statement).one()
    return result

#Creating Data
@app.post("/urls/add")
async def add_url(payload: Urls, token: Token = Depends(get_current_user_token), session: Session = Depends(get_session)):
    if token is None: 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
            detail="Invalid user credentials"
        )
    else:
        new_url = Urls(title=payload.title, long_url=payload.long_url, 
                    short_url=payload.short_url, user_id=payload.user_id)
        session.add(new_url)
        session.commit()
        session.refresh(new_url)
        return {"message": f"Added new url with ID: {new_url.id}"}

@app.post("/register", response_model=UserSchema)
def register_user(payload: UserRegistrationSchema, session: Session = Depends(get_session)):
    payload.hashed_password = User.hash_password(payload.hashed_password)
    return create_user(user+payload, session=session)

@app.post("/login", status_code=200)
async def login(payload: UserAccountSchema, session: session = Depends(get_session)):
    try:
        user: User = get_user(email=payload.email, session=session)
    except: 
        raise HTTPException()

#this needs the login POST added here 

if __name__ == '__main__':
        uvicorn.run('main:app', 
            host='localhost', 
            port=8000,
            reload=True)