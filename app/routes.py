from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserSchema, UserResponse
from app.crud import crud
from typing import List, Union

router = APIRouter()


@router.post("/create")
async def create_user(request: UserSchema, db: Session = Depends(get_db)):
    """
    Create a new user in the database.
    """
    user = crud.create_user(db, user=request)
    return UserResponse(
        status="Ok",
        message="User created successfully",
        code="201",
        result=UserSchema(
            username=user.username
        )
    ).model_dump(exclude_none=True)


@router.get("/", response_model=List[UserSchema])
async def get_users(limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of users.
    """
    return crud.get_users(db, limit=limit)


@router.get("/{user_id}", response_model=Union[UserSchema, dict])
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a user by their ID.
    """
    user = crud.get_user_by_id(db, user_id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
