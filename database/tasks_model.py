from sqlalchemy import Column,Integer,String
from database.db import Base,SessionLocal


class Task(Base):
    __tablename__ = "tasks"

    id=Column(Integer,primary_key=True,autoincrement=True)
    user_id=Column(Integer,nullable=False)
    task=Column(String,nullable=False)
    state=Column(String,nullable=False)

def get_all_tasks(user_id):
    with SessionLocal() as db:
        data=db.query(Task).filter(Task.user_id == user_id).all()
        return data


def get_tasks_bystate(id,state):
    with SessionLocal() as db:
        data=db.query(Task).filter(Task.user_id==id,Task.state == state ).all()
        return data

def add_tasks(user_id,task,state):
    with SessionLocal() as db:
        new_task=Task(
            user_id=user_id,
            task=task,
            state=state
            )
        db.add(new_task)
        db.commit()


def update_task_state(id,task_id,new_state):
    with SessionLocal() as db:
        task=db.query(Task).filter(Task.user_id == id,Task.id == task_id).first()
        if task:
            task.state=new_state
            db.commit()


def delete_task(id,task_id):
    with SessionLocal() as db:
        task=db.query(Task).filter(Task.user_id == id,Task.id == task_id).first()
        if task:
            db.delete(task)
            db.commit()

