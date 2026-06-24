from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.users.schemas import UserCreate
from app.users.service import create_user, get_user_by_email

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def register_user(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = get_user_by_email(db, user.email)

    if existing_user:
        raise HTTPException(status_code=400, detail="Email já registrado")

    new_user = create_user(
        db=db,
        name=user.name,
        email=user.email,
        password=user.password
    )

    return {
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email
    }