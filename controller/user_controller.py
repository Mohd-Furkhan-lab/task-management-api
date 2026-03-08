from services.user_services import user_signup,user_login

def signup(data):
    name=data.get('name')
    email=data.get('email')
    password=data.get('password')
    return user_signup(name,email,password)

def login(data):
    name=data.get("name")
    password=data.get('password')
    return user_login(name,password)