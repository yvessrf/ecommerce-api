from passlib.context import CryptContext

# configura bcrypt
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# hash da senha
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# valida senha
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)