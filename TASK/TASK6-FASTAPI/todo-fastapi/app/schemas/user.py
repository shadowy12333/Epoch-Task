#schemas翻译官，说明书，门卫
from pydantic import BaseModel,Field

class UserCreate(BaseModel):
    username:str=Field(min_length=3,max_length=50)
    password:str=Field(min_length=6,max_length=30)

class UserResponse(BaseModel):
    id:int
    username:str
    model_config={"from_attributes":True}

class Token(BaseModel):
    access_token:str
    token_type:str
