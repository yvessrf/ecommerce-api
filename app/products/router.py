from typing import List, Optional
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.products.schemas import (
    ProductCreate,
    ProductResponse,
    ProductUpdate
)

from app.products.service import create_product, get_products, get_product_by_id, update_product, delete_product

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post(
    "/",
    response_model=ProductResponse
)
def create_new_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    return create_product(
        db=db,
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock
    )

@router.get("/", response_model=List[ProductResponse])
def list_products(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    sort: Optional[str] = None
):
    return get_products(
        db=db,
        skip=skip,
        limit=limit,
        search=search,
        min_price=min_price,
        max_price=max_price,
        sort=sort
    )

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = get_product_by_id(db, product_id)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product não encontrado"
        )

    return product

@router.put("/{product_id}", response_model=ProductResponse)
def update_product_route(
    product_id: int,
    product_data: ProductUpdate,
    db: Session = Depends(get_db)
):
    updated_product = update_product(
        db=db,
        product_id=product_id,
        data=product_data
    )

    if not updated_product:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    return updated_product


@router.delete("/{product_id}")
def delete_product_route(
    product_id: int,
    soft: bool = True,
    db: Session = Depends(get_db)
):
    return delete_product(db, product_id, soft)
