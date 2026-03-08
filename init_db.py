from database.db import engine, Base
from database.tasks_model import Task
from database.user_model import User

Base.metadata.create_all(bind=engine)