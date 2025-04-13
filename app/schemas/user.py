from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    """Input schema for a user"""
    username: str
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
