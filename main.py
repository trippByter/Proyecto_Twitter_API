#===========IMPORTS===========#
#...P Y T H O N 
# UUID
from uuid import UUID
# date
from datetime import date, datetime
# Optional
from typing import Optional, List
#...E X T E R N A L
# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
# FastAPI
from fastapi import FastAPI
from fastapi import status
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

## U S E R S

### /signup
@app.post(
    path = "/signup",
    response_model = User,
    status_code = status.HTTP_201_CREATED,
    summary = "Register a user.",
    tags = ["Users"]
)
def signup():
    pass

### /login
@app.post(
    path = "/login",
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Login a user.",
    tags = ["Users"]
)
def login():
    pass

### /users
@app.get(
    path = "/users",
    response_model = List[User],
    status_code = status.HTTP_200_OK,
    summary = "Show all users.",
    tags = ["Users"]
)
def show_all_users():
    pass

### /users/{user_id}
@app.get(
    path = "/users/{user_id}",
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Show a user.",
    tags = ["Users"]
)
def show_a_user():
    pass

### /users/{user_id}/delete
@app.delete(
    path = "/users/{user_id}/delete",
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Delete a user.",
    tags = ["Users"]
)
def delete_a_user():
    pass

### /users/{user_id}/update
@app.put(
    path = "/users/{user_id}/update",
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Update a user.",
    tags = ["Users"]
)
def update_a_user():
    pass


## T W E E T S

### "/" - Home page. Show all tweets
@app.get(
    path="/",
    response_model = List[Tweet],
    status_code = status.HTTP_200_OK,
    summary = "Show all tweets.",
    tags = ["Tweets"]
)
def home():
    return {"Twitter API": "Wor-king!"}

### "/post" - Post a tweet
@app.post(
    path = "/post",
    response_model = Tweet,
    status_code = status.HTTP_201_CREATED,
    summary = "Post a tweet.",
    tags = ["Tweets"]
)
def post():
    pass

### /tweet/{tweet_id}
@app.get(
    path = "/tweet/{tweet_id}",
    response_model = Tweet,
    status_code = status.HTTP_201_CREATED,
    summary = "Show a tweet.",
    tags = ["Tweets"]
)
def show_a_tweet():
    pass

### /tweet/{tweet_id}/delete
@app.get(
    path = "/tweet/{tweet_id}/delete",
    response_model = Tweet,
    status_code = status.HTTP_200_OK,
    summary = "Delete a tweet.",
    tags = ["Tweets"]
)
def delete_a_tweet():
    pass

### /tweet/{tweet_id}/update
@app.put(
    path = "/tweet/{tweet_id}/update",
    response_model = Tweet,
    status_code = status.HTTP_200_OK,
    summary = "Update a tweet.",
    tags = ["Tweets"]
)
def update_a_tweet():
    pass
#=========FIN PATH OPERATIONS========#