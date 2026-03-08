from fastapi import APIRouter,Request
from controller.user_controller import signup,login
users=APIRouter(prefix="/users",tags=["users"])


@users.post('/login')
async def user_login(request:Request):
    data= await request.json()
    return login(data)


@users.post('/signup')
async def user_signup(request:Request):
    data= await request.json()
    return signup(data)