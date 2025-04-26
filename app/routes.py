from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserSchema, UserCreate, UserResponse
from app.crud import crud
from typing import List, Union

router = APIRouter()


@router.post("/create")
async def create_user(request: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user in the database.
    """
    user = crud.create_user(db, user=request)
    return UserResponse(
        status="Ok",
        message="User created successfully",
        code="201",
        result=UserSchema(
            id=user.id,
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
    user = crud.get_user_by_id(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}", response_model=Union[UserSchema, dict])
async def delete_user(user_id:int, db: Session = Depends(get_db)):
    """
    Deletes a user by their ID.
    """
    user = crud.delete_user(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
