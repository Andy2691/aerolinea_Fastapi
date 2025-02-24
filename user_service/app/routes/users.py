from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from app.auth.auth import hash_password, verify_password, create_access_token
from datetime import timedelta

router = APIRouter()

# Base de datos simulada (temporal)
fake_users_db = {}

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/register")
async def register_user(user: UserCreate):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = hash_password(user.password)
    fake_users_db[user.username] = {"username": user.username, "password": hashed_password}
    
    return {"message": "User registered successfully"}

@router.post("/login")
async def login_user(user: UserLogin):
    user_data = fake_users_db.get(user.username)
    
    if not user_data or not verify_password(user.password, user_data["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token = create_access_token({"sub": user.username}, timedelta(minutes=30))
    
    return {"access_token": access_token, "token_type": "bearer"}
