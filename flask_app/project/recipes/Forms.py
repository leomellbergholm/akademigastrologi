#Authors: Leo M. Holm & Axel Holm
#Coding: utf-8

#################
#### imports ####
#################
from flask_wtf import Form
from wtforms import StringField, BooleanField, SelectField
from .views import Ingredient
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from project import images
from wtforms.ext.sqlalchemy.fields import QuerySelectField
 
class AddRecipeForm(Form):
    recipe_title = StringField('Titel på recept', validators=[DataRequired()])
    recipe_description = StringField('Beskrivning av recept', validators=[DataRequired()]) 
    recipe_image = FileField('Receptbild', validators=[FileRequired(), FileAllowed(images, 'Bara bilder!')])
    is_public = BooleanField('Publikt recept?')


class EditRecipeForm(Form):
    recipe_title = StringField('Titel på recept', validators=[DataRequired()])
    recipe_description = StringField('Beskrivning av recept', validators=[DataRequired()])
    recipe_image = FileField('Receptbild', [FileAllowed(images, 'Bara bilder!')])
    is_public = BooleanField('Publikt recept?')