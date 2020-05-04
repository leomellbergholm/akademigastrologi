#Authors: Leo M. Holm & Axel Holm
#Coding: utf-8

from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email
 
 
class RegisterForm(Form):
    username = StringField('Användarname', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Lösenord', validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Konfirmera lösenord', validators=[DataRequired(), EqualTo('password')])

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Lösenord', validators=[DataRequired()])
