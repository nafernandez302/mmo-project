from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    """Input schema for creating a user"""
    username: str


class UserSchema(UserCreate):
    """Output schema for a user (includes ID)"""
    id: int

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    """Response schema for a user"""
    code: str
    status: str
    message: str
    result: Optional[UserSchema] = None

    class Config:
        orm_mode = True
