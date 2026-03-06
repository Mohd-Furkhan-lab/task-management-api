from fastapi import FastAPI
from routes.tasks import tasks
from routes.users import users

app=FastAPI()
app.include_router(tasks)
app.include_router(users)

def get_app():
    return app