#Authors: Leo M. Holm & Axel Holm & Tamim Nasir
#Coding: utf-8

from project import db, bcrypt, ma
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
from datetime import datetime
from sqlalchemy import create_engine

#databas with sqlalchemy
engine = create_engine('postgresql://ah8140:pzvieemm@pgserver.mah.se/akademigastrologi')
# engine = create_engine('postgresql://aj8578:72w0ljxi@pgserver.mah.se/akademigastrologi2')

class Discussion(db.Model):
    __tablename__="discussion"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, nullable=True)
    forum_id = db.Column(db.Integer, db.ForeignKey('forums.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, comment, forum_id, user_id):
        self.comment = comment
        self.created=datetime.now()
        self.forum_id = forum_id
        self.user_id = user_id

    def __repr__(self):
        return '<id: {}, comment: {}, forum_id: {}, user_id: {}>'.format(self.id, self.comment, self.forum_id, self.user_id)


class Forum(db.Model):

    __tablename__="forums"
    id = db.Column(db.Integer, primary_key=True)
    forum_title = db.Column(db.String, nullable=False)
    forum_description = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created = db.Column(db.DateTime, nullable=True)

    def __init__(self, title, description, user_id):
        self.forum_title = title
        self.forum_description = description
        self.user_id = user_id
        self.created = datetime.now()

    def __repr__(self):
        return '<id: {}, title: {}, description: {}>'.format(self.id, self.forum_title, self.forum_description)

class Ingredient(db.Model):

    __tablename__ = "ingredient"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    measurement_unit = db.Column(db.String, nullable=False)

    def __init__(self, name, measurement_unit):
        self.name = name
        self.measurement_unit = measurement_unit
   
    def __repr__(self):
        return '<id: {}, name: {}, measurement_unit: {}>'.format(self.id, self.name, self.measurement_unit)

class IngredientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ingredient
        include_fk= True

class RecipeHasIngredient(db.Model):

    __tablename__ = "recipe_has_ingredient"
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, recipe_id, ingredient_id, quantity):
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id
        self.quantity = quantity
   
    def __repr__(self):
        return '<recipe_id: {}, ingredient_id: {}, quantity: {}>'.format(self.recipe_id, self.ingredient_id, self.quantity)

    
class Recipe(db.Model):

    __tablename__ = "recipes"
 
    id = db.Column(db.Integer, primary_key=True)
    recipe_title = db.Column(db.String, nullable=False)
    recipe_description = db.Column(db.String, nullable=False)
    is_public = db.Column(db.Boolean, nullable=False)
    image_filename = db.Column(db.String, default=None, nullable=True)
    image_url = db.Column(db.String, default=None, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
 
    def __init__(self, title, description, user_id, is_public, image_filename=None, image_url=None):
        self.recipe_title = title
        self.recipe_description = description
        self.is_public = is_public
        self.image_filename = image_filename
        self.image_url = image_url
        self.user_id = user_id
 
    def __repr__(self):
        return '<id: {}, title: {}, user_id: {}>'.format(self.id, self.recipe_title, self.user_id)


class User(db.Model):
 
    __tablename__ = 'users'
 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    registered_on = db.Column(db.DateTime, nullable=True)
    last_logged_in = db.Column(db.DateTime, nullable=True)
    current_logged_in = db.Column(db.DateTime, nullable=True)
    role = db.Column(db.String, default='user')
    recipes = db.relationship('Recipe', backref='user', lazy='dynamic')


    def __init__(self, username, email, password_plaintext, role='user'):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password_plaintext).decode('UTF-8')
        self.authenticated = False
        self.registered_on = datetime.now()
        self.last_logged_in = None
        self.current_logged_in = datetime.now()
        self.role = role

    @hybrid_method
    def is_correct_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
 
    @property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated
 
    @property
    def is_active(self):
        """Always True, as all users are active."""
        return True
 
    @property
    def is_anonymous(self):
        """Always False, as anonymous users aren't supported."""
        return False
 
    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        """Requires use of Python 3"""
        return str(self.id)
 
    def __repr__(self):
        return '<User {0}>'.format(self.username)
