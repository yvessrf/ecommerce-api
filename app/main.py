from fastapi import FastAPI
from app.users.router import router as users_router

app = FastAPI(
    title="Ecommerce API",
    version="1.0.0"
)

app.include_router(users_router)

@app.get("/")
def root():
    return {"message": "Ecommerce API Online"}