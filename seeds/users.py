from app.models import db, environment, SCHEMA
from app.models.db import User
from sqlalchemy.sql import text
import datetime


def seed_users():
    for user in users:
        new_user = User(
            username = user["username"],
            password = user["password"],
            email = user["email"],
            first_name = user["first_name"],
            last_name=user["last_name"],
            buying_power=user["buying_power"],
            title=user["title"],
            created_at=user["created_at"],
            updated_at=user["updated_at"]
        )
        db.session.add(new_user)

    db.session.commit()