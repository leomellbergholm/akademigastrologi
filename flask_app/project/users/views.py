from flask import Flask, render_template, Blueprint, request, flash, redirect, url_for, abort
from project import db #, mail
from .Forms import RegisterForm, LoginForm
from project.models import User
from sqlalchemy.exc import IntegrityError
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from datetime import datetime
#from flask_mail import Mail, Message


users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                new_user = User(form.email.data, form.password.data)
                new_user.authenticated = True
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)

                # send_confirmation_email(new_user.email)

                flash('Tack, du är nu registrerad!', 'success')
                return redirect(url_for('recipes.public_recipes'))
                
            except IntegrityError:
                db.session.rollback()
                flash('Fel! Emailen ({}) finns redan.'.format(form.email.data), 'error')
    return render_template('register.html', form=form)

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user is not None and user.is_correct_password(form.password.data):
                user.authenticated = True
                user.last_logged_in = user.current_logged_in
                user.current_logged_in = datetime.now()
                db.session.add(user)
                db.session.commit()
                login_user(user)
                flash('Thanks for logging in, {}'.format(current_user.email))
                return redirect(url_for('recipes.public_recipes'))
            else:
                flash('Oj, någonting i dina uppgifter var fel!', 'error')
    return render_template('login.html', form=form)

@users_blueprint.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    flash('Välkommen tillbaka!', 'info')
    return redirect(url_for('users.login'))

@users_blueprint.route('/user_profile')
@login_required
def user_profile():
    return render_template('user_profile.html')

@users_blueprint.route('/admin_view_users')
@login_required
def admin_view_users():
    if current_user.role != 'admin':
        abort(403)
    else:
        users = User.query.order_by(User.id).all()
        return render_template('admin_view_users.html', users=users)
    return redirect(url_for('stocks.watch_list'))



