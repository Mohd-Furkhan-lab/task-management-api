from database.user_model import add_user,login_verification,get_user_id
from middelware.jwt import create_jwt_token
import bcrypt

def user_signup(name,email,password):
    passw=password.encode('utf-8')
    hash=bcrypt.hashpw(passw,bcrypt.gensalt())
    res= add_user(name,email,hash)
    return {"Message":"Added Successfully"}


def user_login(name,password):
    stored_password=login_verification(name)
    if stored_password:
        password_bytes=password.encode('utf-8')
        res=bcrypt.checkpw(password_bytes,stored_password)
        if res:
            user_id=get_user_id(res,name)
            token=create_jwt_token(user_id)
            return token
        else:
            return {"Message":"Wrong Password"}
    else:
        return {"Message":"No User Found"}