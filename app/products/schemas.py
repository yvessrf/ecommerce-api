from pydantic import BaseModel
from typing import Optional


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock:int


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int

    model_config = {
        "from_attributes": True
    }

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None