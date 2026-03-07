from database.db import engine, Base
from database.tasks_model import Task

Base.metadata.create_all(bind=engine)