#coding=utf-8
from flask import render_template,redirect , request , url_for , flash
from flask_login import login_user,login_required,logout_user,current_user
from . import auth
from ..models import User
from .forms import LoginForm,RegistrationForm,confirmEmailForm,resetPasswordForm
from ..main import main
from app import db
from ..email import send_email
#
# @app.route('/secret')
# @login_required
# def secret():
#     return "Only authenticated users are allowed!"



@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Confirm Your Account','auth/email/confirm', user=current_user, token=token)
    flash('A new confirmation email has been sent to you by email.')
    return redirect(url_for('main.index'))

@auth.before_app_request
def before_request():
    if current_user.is_authenticated \
        and not current_user.confirmed \
        and request.endpoint[:5] != 'auth.'\
        and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirmed'))
@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html',user=current_user.username)

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('You have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('main.index'))

@auth.route('/modifyPassword/<token>',methods=['GET','POST'])
def modifyPassword(token):
    form = resetPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            user.reset_password(form.password.data)
            flash(u'密码已修改，请使用新密码登录')
            return redirect(url_for('auth.login'))
    return render_template('auth/resetPassword.html',form=form)

@auth.route('/confirmEmail/',methods=['GET','POST'])
def confirmEmail():
    form = confirmEmailForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.username == form.username.data:
            token = user.generate_confirmation_token()
            send_email(user.email, u'重置密码','auth/email/confirmEmail', user=user, token=token)
            flash(u'一封邮件已经发送到您的邮箱，请点击邮箱内的链接修改密码')
            return redirect(request.args.get('next') or url_for('auth.confirmEmail'))
        flash(u'邮箱或用户名错误，请核对后重新提交')
    return render_template('auth/confirmEmail.html',form = form)

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm();
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
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
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, 'Confirm Your Account','auth/email/confirm', user=user, token=token)
        flash('A confirmation email has been sent to you by email.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
