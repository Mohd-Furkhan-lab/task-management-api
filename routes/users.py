from fastapi import APIRouter

users=APIRouter(prefix="/users",tags=["users"])


@users.post('/login')
def user_login():
    return "User Login"


@users.post('/signup')
def user_signup():
    return "User Signup"