#Authors: Tamim Nasir
#Coding: utf-8

#################
#### imports ####
#################
 
from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from .Forms import AddTopic
from project.models import Forum, User
from project import db

################
#### config ####
################
 
forums_blueprint = Blueprint('forums', __name__)
 
 
################
#### routes ####
################
@forums_blueprint.route('/forums')
def forum():
    # all_forums = Forum.query.all()
    all_forums = db.session.query(Forum, User).join(User).order_by(Forum.id.desc())
    return render_template('forum.html', all_forums=all_forums)

@forums_blueprint.route('/addTopic', methods=['POST'])
@login_required
def add_topic():
    form2 = AddTopic()
    if request.method == 'POST':
        new_topic = Forum(form2.question_title.data, form2.main_question.data, current_user.id)
        db.session.add(new_topic)
        db.session.commit()

        return forum()


