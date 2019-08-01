import logging
import time

from flask import session
from flask_security import login_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

from logsys.users.models import User


class LoginForm(FlaskForm):
    """
    登录表单
    """
    email = StringField('用户名', validators=[DataRequired('用户名不能为空')])
    password = PasswordField('密码', validators=[DataRequired('密码不能为空')])

    def __init__(self, *args, **kwargs):
        """create instance"""
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        initial_validation = super(LoginForm, self).validate()

        logging.info('登录信息校验')

        self.user = User.objects(email=self.email.data).first()
        # 判断用户是否存在
        if self.user:
            if not self.user.check_password(self.password.data):
                self.password.errors.append('密码错误')
                initial_validation = False
        else:
            self.email.errors.append("用户不存在")
            initial_validation = False

        logging.info('登录校验结果')
        logging.info(initial_validation)

        if not initial_validation:
            return False

        login_user(self.user)

        session['auth_token'] = self.user.get_auth_token()
        session['auth_token_time'] = int(round(time.time()))
        # session['email'] = self.user.email.data

        return initial_validation


class RegisterForm(FlaskForm):
    """
    注册表单
    """
    email = StringField('用户名', validators=[DataRequired('用户名不能为空')])
    password = PasswordField('密码', validators=[DataRequired('密码不能为空'), EqualTo('re_password', message='两次输入密码不一致')])
    re_password = PasswordField('确认密码', validators=[DataRequired('确认密码不能为空')])

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """validate the form"""
        inital_validation = super(RegisterForm, self).validate()

        # 验证用户名
        self.user = User.objects(email=self.email).first()
        if self.user:
            self.email.errors.append('用户名已存在')
        if not inital_validation:
            return False

        if len(self.errors) > 0:
            return False

        return True
