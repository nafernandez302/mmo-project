"""Module with crud operations"""

from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserSchema


def create_user(db: Session, user: UserSchema):
    """Create a new user in the database."""
    _user = User(
        username=user.username
    )
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user
