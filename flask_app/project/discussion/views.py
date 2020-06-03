#Authors: Tamim Nasir
#Coding: utf-8

#################
#### imports ####
#################
 
from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from .Forms import AddComment
from project.models import Discussion, Forum, User
from project import db

################
#### config ####
################
 
discussion_blueprint = Blueprint('discussion', __name__)
 
 
################
#### routes ####
################
@discussion_blueprint.route('/discussion/<forum_id>')
def discussion(forum_id):
    discussions = db.session.query(Discussion, User).join(User).filter(Discussion.forum_id == forum_id).order_by(Discussion.id.asc())
    forum_infos = db.session.query(Forum, User).join(User).filter(Forum.id == forum_id)
    return render_template('discussion.html', discussions=discussions, forum_infos=forum_infos, forum_no=forum_id)

@discussion_blueprint.route('/AddComment/<forum_id>', methods=['POST'])
@login_required
def add_comment(forum_id):
    form = AddComment()
    if request.method == 'POST':
        new_comment = Discussion(form.comment.data, forum_id, current_user.id)
        db.session.add(new_comment)
        db.session.commit()
        return discussion(forum_id)
        # return render_template('forum.html', message='greate success')

