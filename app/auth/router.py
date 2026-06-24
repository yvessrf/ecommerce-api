from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.users.schemas import UserLogin
from app.users.service import get_user_by_email

from app.auth.security import verify_password
from app.auth.jwt import create_access_token
from app.auth.dependencies import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login")
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db)
):

    user = get_user_by_email(
        db,
        user_data.email
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Credenciais Inválidas"
        )

    valid_password = verify_password(
        user_data.password,
        user.password
    )

    if not valid_password:
        raise HTTPException(
            status_code=401,
            detail="Credenciais Inválidas"
        )

    access_token = create_access_token(
        data={
            "sub": user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get("/me")
def get_me(
    current_user: str = Depends(get_current_user)
):
    return {
        "email": current_user
    }