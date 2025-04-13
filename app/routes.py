from app.crud import crud
from app.database import get_db
from app.schemas.user import UserSchema, UserResponse
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
router = APIRouter()


@router.post("/create")
async def create_user(request: UserSchema, db: Session = Depends(get_db)):
    crud.create_user(db, user=request)
    print(request)
    return UserResponse(status="Ok",
                    code="200",
                    message="User created successfully",result=request).dict(exclude_none=True)

