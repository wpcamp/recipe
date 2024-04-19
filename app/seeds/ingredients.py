from app.models import db, environment, SCHEMA
from app.models.db import Ingredient
from sqlalchemy.sql import text
from .data import ingredients

def seed_ingredients():
    for ingredient in ingredients:
        new_ingredient = Ingredient(
            user_id=ingredient["user_id"],
            name=ingredient["name"],
        )
        db.session.add(new_ingredient)
    db.session.commit()

def undo_ingredients():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.ingredients RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM ingredients"))

    db.session.commit()

