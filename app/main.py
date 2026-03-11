from fastapi import FastAPI
from routes.tasks import tasks
from routes.users import users
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks)
app.include_router(users)

def get_app():
    return app