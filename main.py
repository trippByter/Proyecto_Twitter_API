#===========IMPORTS===========#
#...P Y T H O N 
# JSON
import json
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
from fastapi import Body, FastAPI
from fastapi import status
#==========FIN IMPORTS========#

app = FastAPI();

#=============MODELS============#
# Los modelos van entre "app" y las path operations

# U S E R S
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


class UserRegister(User):
    # Hereda de UserBase
    # y adiciona atributo "password"
    password: str = Field(
        ..., 
        min_length=8, 
        max_length=30,
    )


# T W E E T S
class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ..., 
        min_length=1, 
        max_length=256
    )
    # Fecha y hora de creación de tweeter
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
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
def signup(user: UserRegister = Body(...)):
    """
    SignUp.

    This path operation register a user in the app.
    
    Parameters:
        - Request **body** parameter:
            - user: UserRegister.
    
    Returns a **JSON** with the basic user information: 
       **{**
            **user_id   : UUID,**
            **email     : EmailStr,**
            **first_name: str,**
            **last_name : str,**
            **birth_date: Optional[date]**
        **}**
    """
    # Abrimos "users.json" || "r+" -> Lectura y escritura 
    with open("users.json", "r+", encoding="utf-8") as f:
        # f.read() -> str ((conv dicc/JSON)) -> json.loads()
        # "results" -> lista de diccionarios (user.json->[])
        results = json.loads(f.read())
        
        # req body data => str/py dict => append "results" -> user.json
        # JSON user param(request body) => dict
        user_dict = user.dict()
        # Transformar datos no string a JSON 
        # user_id: UUID -> str 
        # birht_date: date -> str
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        # Colocarnos al principio del archivo
        # para no escribir en la ubicación del archivo
        f.seek(0)
        # convertimos lista de diccionarios a JSON
        f.write(json.dumps(results))
        
        return user

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
    """
    Show all users.

    This path operation shows all users in the app.

    Parameters:
        -
    
    Returns a **JSON** list with all users in the app, with the following keys:
        **{**
            **user_id   : UUID,**
            **email     : EmailStr,**
            **first_name: str,**
            **last_name : str,**
            **birth_date: datetime**
        **}**
    """
    # Abrimos el users.json en modo lectura
    with open("users.json", "r", encoding="utf-8") as f:
        # Es un simil a JSON - lista de diccionarios
        results = json.loads(f.read())
        return results

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
    """
    Show all tweets.

    This path operation shows all tweets in the app.

    Parameters:
        -
    
    Returns a **JSON** list with all tweets in the app, with the following keys:
        **{**
            **tweet_id: UUID,**
            **content: str,**
            **created_at: datetime,**
            **updated_at: Optional[datetime],**
            **by: User**
        **}**
    """
    # Abrimos el users.json en modo lectura
    with open("tweets.json", "r", encoding="utf-8") as f:
        # Es un simil a JSON - lista de diccionarios
        results = json.loads(f.read())
        return results

### "/post" - Post a tweet
@app.post(
    path = "/post",
    response_model = Tweet,
    status_code = status.HTTP_201_CREATED,
    summary = "Post a tweet.",
    tags = ["Tweets"]
)
def post(tweet: Tweet = Body(...)):
    """
    Post a Tweet.

    This path operation post a tweet in the app.
    
    Parameters:
        - Request **body** parameter:
            - tweet: Tweet.
    
    Returns a **JSON** with the basic tweet information: 
       **{**
            **tweet_id: UUID,**
            **content: str,**
            **created_at: datetime,**
            **updated_at: Optional[datetime],**
            **by: User**
        **}**
    """
    # Abrimos "tweets.json" || "r+" -> Lectura y escritura 
    with open("tweets.json", "r+", encoding="utf-8") as f:
        # f.read() -> str ((conv dicc/JSON)) -> json.loads()
        # "results" -> lista de diccionarios (user.json->[])
        results = json.loads(f.read())
        
        # req body data => str/py dict => append "results" -> tweets.json
        # JSON tweet param(request body) => dict
        tweet_dict = tweet.dict()
        # Transformar datos no string a JSON
        # tweet_id: UUID -> str
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        # created_at: datetime -> str
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        # updated_at: datetime -> str
        tweet_dict["updated_at"] = str(tweet_dict["updated_at"])
        # by: User -> str
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])
        results.append(tweet_dict)
        # Colocarnos al principio del archivo
        # para no escribir en la ubicación del archivo
        f.seek(0)
        # convertimos lista de diccionarios a JSON
        f.write(json.dumps(results))
        
        return tweet

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