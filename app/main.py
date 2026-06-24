from fastapi import FastAPI
from app.users.router import router as users_router
from app.auth.router import router as auth_router
from app.products.router import router as products_router


app = FastAPI(
    title="Ecommerce API",
    version="1.0.0"
)

app.include_router(users_router)
app.include_router(auth_router)
app.include_router(products_router)

@app.get("/")
def root():
    return {"message": "Ecommerce API Online"}