#Authors: Leo M. Holm & Axel Holm
#Coding: utf-8

#################
#### imports ####
#################
from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from project import images
 
class AddRecipeForm(Form):
    recipe_title = StringField('Titel på recept', validators=[DataRequired()])
    recipe_description = StringField('Beskrivning av recept', validators=[DataRequired()])
    recipe_image = FileField('Receptbild', validators=[FileRequired(), FileAllowed(images, 'Bara bilder!')])
    is_public = BooleanField('Publikt recept?')