from fastapi import FastAPI, Depends, HTTPException, status
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer 
from datetime import datetime, timedelta, timezone

import config

from pydantic import BaseModel


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
    return {"message": "Beginning of the Plants"}

@app.post("/create")
async def create_plant(
     common_name: str, 
     scientific_name: str, 
     purchase_location: str,
     purchase_date: int,
         ): 
    plant = plant(common_name=common_name,
                    scientific_name=scientific_name, 
                    purchase_location=purchase_location,
                    purchase_date=purchase_date )
    session.add(plant)
    session.commit()
    return {"Plant added": plant.common_name}
                  

#put is to update the plant status

    common_name: str
    scientific_name: str
    purchase_location: str
    purchase_date: int
#this needs the login POST added here 

if __name__ == '__main__':
        uvicorn.run('main:app', 
            host='localhost', 
            port=8000,
            reload=True)