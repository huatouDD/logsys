import logging

from flask import Blueprint, request, render_template, session
from flask_security import logout_user

from logsys.public.forms import LoginForm

blueprint = Blueprint('public', __name__, static_folder='../static')


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """
    登录界面
    :return:
    """
    logging.info('调转至登录页面')
    print('---------------------!!!!!!!!!!!!!!!!!!!!!!')
    logout_user()
    session.clear()
    form = LoginForm()
    return render_template('login.html', login_form=form)