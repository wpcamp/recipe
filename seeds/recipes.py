from app.models import db, environment, SCHEMA
from app.models.db import Recipe
from sqlalchemy.sql import text
from .data import recipes


def seed_recipes():
    for recipe in recipes:
        new_recipe = Recipe(
            user_id=recipe["user_id"],
            name=recipe["name"],
            description=recipe["description"],
            cuisine_tag=recipe["cuisine_tag"],
            dietary_tag=recipe["dietary_tag"],
            taste_tag=recipe["taste_tag"],
        )
        db.session.add(new_recipe)
    db.session.commit()


def undo_recipes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.recipes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM recipes"))

    db.session.commit()

