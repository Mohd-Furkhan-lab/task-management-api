from sqlalchemy import Column,Integer,String
from database.db import Base,SessionLocal


class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String,nullable=False)
    email=Column(String,nullable=False)
    password=Column(String,nullable=False)


def add_user(name,email,password):
    with SessionLocal() as db:
        new_user=User(
            name=name,
            email=email,
            password=password
        )
        db.add(new_user)
        db.commit()

def login_verification(name):
    with SessionLocal() as db:
         password=db.query(User.password).filter(User.name == name).scalar()
         return password

def get_user_id(isverified,name):
    with SessionLocal() as db:
        if isverified:
            usid=db.query(User.id).filter(User.name == name).scalar()
            return usid