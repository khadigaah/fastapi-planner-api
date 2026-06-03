from database.connection import Database
from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn, UserSignup

user_router = APIRouter(tags=["users"])

user_database = Database(User)


@user_router.post("/signup")
async def sign_new_user(user: UserSignup) -> dict:
    user_exists = await user_database.find_one(User.email == user.email)
    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )
    await user_database.save(user)
    return {"message": "User signed up successfully"}

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    user_exists = await user_database.find_one(User.email == user.email)
    if not user_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    if user_exists.password == user.password:
        return {"message": "User signed in successfully"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials"
    )