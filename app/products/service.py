from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from app.products.models import Product
from fastapi import HTTPException


def create_product(
    db: Session,
    name: str,
    description: str,
    price: float,
    stock: int
):
    product = Product(
        name=name,
        description=description,
        price=price,
         stock=stock
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product

def get_products(
    db: Session, 
    skip: int = 0, 
    limit: int = 10, 
    search: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    sort: str | None = None
):
    query = db.query(Product)
    if search:
        query = query.filter(Product.name.ilike(f"%{search}%"))

    if min_price is not None:
        query = query.filter(Product.price >= min_price)

    if max_price is not None:
        query = query.filter(Product.price <= max_price)

    if sort == "price_asc":
        query = query.order_by(asc(Product.price))

    elif sort == "price_desc":
        query = query.order_by(desc(Product.price))

    return query.offset(skip).limit(limit).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product(db: Session, product_id: int, data):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        return None

    if data.name is not None:
        product.name = data.name

    if data.description is not None:
        product.description = data.description

    if data.price is not None:
        product.price = data.price

    if data.stock is not None:
        product.stock = data.stock

    db.commit()
    db.refresh(product)

    return product

def delete_product(db: Session, product_id: int, soft: bool = True):

    product = db.query(Product).filter(Product.id == product_id).first()
    print("ID recebido:", product_id)
    print("Produto encontrado:", product)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if soft:
        product.is_active = False
        db.commit()
        return {"message": "Product soft deleted"}

    db.delete(product)
    db.commit()

    return {"message": "Product deleted permanently"}