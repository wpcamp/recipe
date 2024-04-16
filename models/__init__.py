from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

import os

environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")
db = SQLAlchemy()


def add_prefix_for_prod(attr):
    if environment == "production":
        return f"{SCHEMA}.{attr}"
    else:
        return attr


# ==================================== User Model ====================================

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    ingredients = db.relationship('Ingredient', backref='user')
    recipes = db.relationship('Recipe', backref='user')
    dietary_preferences = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'password': self.password,
            'dietary_preferences': self.dietary_preferences,
            'recipes': self.recipes,
            'ingredients': self.ingredients
        }


# ==================================== Ingredient Model ====================================

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name
        }


# ==================================== Recipe Model ====================================


class Recipe(db.Model):
    recipe_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'), nullable=False)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    cuisine_tag = db.Column(db.String(255))
    dietary_tag = db.Column(db.String(255))
    taste_tag = db.Column(db.String(255))
    prep_time = db.Column(db.String(255))
    cooking_time = db.Column(db.String(255))
    servings = db.Column(db.String(255))
    recipe_ingredients = db.relationship(
        'RecipeIngredient', backref='recipe')

    def to_dict(self):
        return {
            'recipe_id': self.recipe_id,
            'user_id': self.user_id,
            'name': self.name,
            'description': self.description,
            'cuisine_tag': self.cuisine_tag,
            'dietary_tag': self.dietary_tag,
            'taste_tag': self.taste_tag,
            'prep_time': self.prep_time,
            'cooking_time': self.cooking_time,
            'servings': self.servings,
        }
