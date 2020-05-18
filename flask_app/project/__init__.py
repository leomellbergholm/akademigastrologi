#Authors: Leo M. Holm & Axel Holm
#Coding: utf-8

#################
#### imports ####
#################
 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#from flask_mail import Mail
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_bcrypt import Bcrypt

################
#### config ####
################
 
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')
bcrypt = Bcrypt(app)
 
db = SQLAlchemy(app)
#mail = Mail(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"

# Configure the image uploading via Flask-Uploads
images = UploadSet('images', IMAGES)
configure_uploads(app, images) 
 

from project.models import User
 
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
 
 
####################
#### blueprints ####
####################
 
from project.users.views import users_blueprint
from project.recipes.views import recipes_blueprint
from project.forums.views import forums_blueprint

# register the blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(recipes_blueprint)
app.register_blueprint(forums_blueprint)


############################
#### custom error pages ####
############################
from flask import Flask, render_template

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
 
 
@app.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403
 
 
@app.errorhandler(410)
def page_not_found(e):
    return render_template('410.html'), 410