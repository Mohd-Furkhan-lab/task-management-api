from functools import wraps
from fastapi import Request
from fastapi.responses import JSONResponse
from middelware.jwt import verify_jwt_token

def jwt_required(func):

    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return JSONResponse({"message": "Token missing"}, status_code=401)

        token = auth_header.split(" ")[1]

        payload = verify_jwt_token(token)

        if not payload:
            return JSONResponse({"message": "Invalid or expired token"}, status_code=401)

        request.state.user = payload["user_id"]

        return await func(request, *args, **kwargs)

    return wrapper