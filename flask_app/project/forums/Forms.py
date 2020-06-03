#Authors: Tamim Nasir
#Coding: utf-8

#################
#### imports ####
#################
from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class AddTopic(Form):
    question_title = StringField('Question Title', validators=[DataRequired()])
    main_question = StringField('Question', validators=[DataRequired()])