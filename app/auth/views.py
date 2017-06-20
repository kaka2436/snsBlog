from flask import render_template,redirect , request , url_for , flash
from flask_login import login_user,login_required,logout_user
from . import auth
from ..models import User
from .forms import LoginForm,RegistrationForm
from ..main import main
from app import db

#
# @app.route('/secret')
# @login_required
# def secret():
#     return "Only authenticated users are allowed!"

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm();
    print "000"
    if form.validate_on_submit():
        print "111"
        user = User.query.filter_by(email=form.email.data).first()
        print "222"
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            print "333"
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

@auth.route('/register',methods=['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
