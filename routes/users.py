from fastapi import APIRouter, HTTPException, status
from models.users import UserSignIn, UserSignup

user_router = APIRouter(tags=["users"])

# Simulated database
users = {}

@user_router.post("/signup")
async def sign_new_user(data: UserSignup) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )
    users[data.email] = data
    return {"message": "User created successfully"}

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password"
        )
    return {"message": "User signed in successfully"}