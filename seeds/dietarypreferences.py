from app.models import db, environment, SCHEMA
from app.models.db import DietaryPreference
from sqlalchemy.sql import text
from .data import dietary_preferences
import datetime

def seed_dietary_preferences():
    for dietary_preference in dietary_preferences:
        new_dietary_preference = DietaryPreference(
            name = dietary_preference["name"]
        )
        db.session.add(new_dietary_preference)

    db.session.commit()


def undo_dietary_preferences():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.dietary_preferences RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM dietary_preferences"))
    
    db.session.commit()

    