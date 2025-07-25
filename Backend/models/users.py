
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name:str
    email: EmailStr
    password: str

class UserInDB(UserCreate):
    role: str = "user"

class UserLogin(BaseModel):
    email: EmailStr
    password: str
