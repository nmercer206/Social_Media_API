from tokenize import String
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

# WE WANT TO CREATE DIFFERENT MODELS FOR DIFFERENT REQUESTS, IN ORDER TO SPECIFY WHAT THE USER CAN OR CAN'T CHANGE WITHIN OUR TABLES

class Post(BaseModel): # BaseModel makes it so that the input parameters for the request are bound to a data type, so if the user enters something else in, it'll throw an error.
    title: str         # This is a pydantic model. Think of it as a cast to every request
    content: str
    published: bool = True #resorts to 'True' if user doesn't input anything in


class PostBase(BaseModel):
    title: str         
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass



class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class Post(PostBase):   # since this class inherits from PostBase, it inherits all of it's properties
    id: int             # (title, content, published), so we don't need to specify those fields
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

