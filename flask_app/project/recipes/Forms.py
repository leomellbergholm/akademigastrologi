from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
 
 
class AddRecipeForm(Form):
    recipe_title = StringField('Titel på recept', validators=[DataRequired()])
    recipe_description = StringField('Beskrivning av recept', validators=[DataRequired()])