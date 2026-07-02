from fastapi import FastAPI, APIRouter, Request, Response, Depends
from pydantic import BaseModel
from typing import List, Optional

from app import crud

app = FastAPI()

app.include_router(crud.router)

    
    