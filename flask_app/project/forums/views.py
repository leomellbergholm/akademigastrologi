#Authors: Leo M. Holm & Axel Holm
#Coding: utf-8

#################
#### imports ####
#################
 
from flask import render_template, Blueprint, request, flash, redirect, url_for
from project.models import Forum
# from .Forms import AddRecipeForm
from project import db
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from flask_uploads import UploadSet, IMAGES, configure_uploads  

################
#### config ####
################
 
forums_blueprint = Blueprint('forums', __name__)
 
 
################
#### routes ####
################
@forums_blueprint.route('/forums')
def forum():
    all_forums = Forum.query.all()
    return render_template('forum.html', all_forums=all_forums)

