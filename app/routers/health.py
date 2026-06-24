from fastapi import APIRouter
from sqlalchemy import text

from app.db.database import SessionLocal

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
def health():
    return {"status": "ok"}


@router.get("/db")
def health_db():
    try:
        db = SessionLocal()

        db.execute(text("SELECT 1"))

        return {
            "status": "ok",
            "database": "connected"
        }

    except Exception as e:
        return {
            "status": "error",
            "database": str(e)
        }

    finally:
        db.close()