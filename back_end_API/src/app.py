from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from clerk_backend_api import Clerk
import os

clerk_sdk = Clerk(bearer_auth=os.getenv("CLERK_SECRET-KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"]
    )
# origins should be the local host we are using, ie 5174, for now asterisk allows everything, just to prevent errors. 

