from app.models import db, environment, SCHEMA
from app.models.db import User
from sqlalchemy.sql import text
from .data import users
import datetime


def seed_users():
    for user in users:
        new_user = User(
            username = user["username"],
            password = user["password"],
            email = user["email"],
            first_name = user["first_name"],
            dietary_preferences = user["dietary_preferences"],
            recipes = user["recipes"] 
        )
        db.session.add(new_user)

    db.session.commit()

def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
    
    db.session.commit()

    