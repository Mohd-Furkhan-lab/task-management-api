import jwt 
from datetime import datetime,timedelta

SECRET_KEY = "4d9f2b4c6a0f9d2e8c7b6a5e3d2c1f9a4b7c6d5e3a1f2c9b8e7d6a5c4b3a2f1"
ALGORITHM="HS256"

def create_jwt_token(user_id):
    payload={
        "user_id":user_id,
        "exp":datetime.utcnow()+timedelta(hours=1)
    }
    token=jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    return token

def verify_jwt_token(token):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None