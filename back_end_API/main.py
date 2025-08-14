from fastapi import FastAPI, Depends, HTTPException, status
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer 
from datetime import datetime, timedelta, timezone

import config




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


#this needs the login POST added here 

if __name__ == '__main__':
        uvicorn.run('main:app', 
            host='localhost', 
            port=8000,
            reload=True)