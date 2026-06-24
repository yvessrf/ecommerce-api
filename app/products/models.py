from datetime import datetime

from sqlalchemy import  Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Product(Base):

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(150))

    description: Mapped[str] = mapped_column(String(500))

    price: Mapped[float] = mapped_column(Float)

    stock: Mapped[int] = mapped_column(Integer)

    is_active = Column(Boolean, default=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    
    
    