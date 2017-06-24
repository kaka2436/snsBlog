#coding=utf-8
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm as Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Length,Email
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class resetPasswordForm(FlaskForm):
    username = StringField(u'用户名',validators=[
        Required(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Usernames must have only letters, ''numbers, dots or underscores')
    ])
    password = PasswordField(u'密码',validators=[
    Required(),EqualTo('password2', message='Passwords must match.')
    ])
    password2 = PasswordField(u'密码',validators=[
    Required()
    ])
    submit = SubmitField(u'确定')

class confirmEmailForm(FlaskForm):
    username = StringField(u'用户名',validators=[
        Required(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Usernames must have only letters, ''numbers, dots or underscores')
    ])
    email = StringField(u'邮箱',validators=[
        Required(),Length(1,64),Email()
    ])
    submit = SubmitField(u'确定')

class LoginForm(FlaskForm):
    email = StringField(u'邮箱',validators=[
    Required(),Length(1,64),Email()
    ])
    password = PasswordField(u'密码',validators=[
    Required()
    ])
    remember_me = BooleanField(u'保持登录')
    submit = SubmitField(u'登录')


class RegistrationForm(Form):
    email = StringField(u'邮箱', validators=[Required(), Length(1, 64),Email()])
    username = StringField(u'用户名', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Usernames must have only letters, ''numbers, dots or underscores')])
    password = PasswordField(u'密码', validators=[Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField(u'确认密码', validators=[Required()])
    submit = SubmitField(u'注册')
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'邮箱已注册')
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(u'用户名已被占用')
