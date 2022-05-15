#===========IMPORTS===========#
#...P Y T H O N 
# UUID
from uuid import UUID
# date
from datetime import date, datetime
# Optional
from typing import Optional
#...E X T E R N A L
# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
# FastAPI
from fastapi import FastAPI
#==========FIN IMPORTS========#

app = FastAPI();

#=============MODELS============#
# Los modelos van entre "app" y las path operations
class UserBase(BaseModel):
    # Universal Unit ID
    user_id: UUID = Field(...)
    email: EmailStr = Field(...) 


class UserLogin(UserBase):
    password: str = Field(
        ..., 
        min_length=8, 
        max_length=30,
    )


class User(UserBase):
    first_name: str = Field(
        ...,
        min_legth=1,
        max_length=30,
    )
    last_name: str = Field(
        ...,
        min_legth=1,
        max_length=30,
    )
    birth_date: Optional[date] = Field(default=None) 


class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ..., 
        min_length=1, 
        max_length=256
    )
    # Fecha y hora de creación de tweeter
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)
#============FIN MODELS===========#


#==========PATH OPERATIONS==========#
# Path Operation del home page
@app.get(path="/")
def home():
    return {"Twitter API": "Wor-king!"}
#=========FIN PATH OPERATIONS========#