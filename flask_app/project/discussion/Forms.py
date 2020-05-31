#Authors: Tamim Nasir
#Coding: utf-8

#################
#### imports ####
#################
from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class AddComment(Form):
    comment = StringField('Add a comment', validators=[DataRequired()])
