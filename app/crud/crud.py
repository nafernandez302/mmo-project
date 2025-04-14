"""Module with crud operations"""

from fastapi import HTTPException
from sqlalchemy import Integer
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserSchema


def create_user(db: Session, user: UserSchema):
    """Create a new user in the database."""
    _user = User(
        username=user.username
    )
    try:
        db.add(_user)
        db.commit()
        db.refresh(_user)
        return _user
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=400, detail="Username already exists") from exc
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}") from e

def get_user_by_id(db: Session, user_id: Integer):
    """Get user information by id."""
    return db.query(User).filter(User.id == user_id)

def get_users(db: Session, limit: int=100):
    """Get all users."""
    return db.query(User).limit(limit).all()
