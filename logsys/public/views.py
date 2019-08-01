import logging
from flask import Blueprint, request, render_template, session, jsonify
from flask_security import logout_user

from logsys import response
from logsys.extensions import csrf_protect
from logsys.public.forms import LoginForm, RegisterForm
from logsys.users.models import User

blueprint = Blueprint('public', __name__, static_folder='../static')


@csrf_protect.exempt
@blueprint.route('/')
@blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    """
    登录界面
    :return:
    """
    logging.info('调转至登录页面')
    logout_user()
    session.clear()
    form = LoginForm()
    return render_template('login.html', login_form=form)


@csrf_protect.exempt
@blueprint.route('/login_api/', methods=["GET", "POST"])
def login_api():
    """
    登录验证
    :return:
    """
    logging.info('正在验证用户')
    resp_data = {}
    try:
        form = LoginForm()
        if request.method == "POST":
            # 验证登录信息
            if form.validate_on_submit():
                resp_data["code"] = response.SUCCESS
                resp_data["msg"] = response.RESULT_SUCCESS
                resp_data["data"] = []
            else:
                resp_data["code"] = response.PARAMETER_ERROR
                resp_data["msg"] = response.RESULT_PARAMETER_ERROR
                resp_data["data"] = {'password': form.password.errors}
    except Exception as e:
        logging.error(e)
        resp_data["code"] = response.ERROR
        resp_data["msg"] = []
        resp_data["data"] = response.RESULT_ERROR
    finally:
        return jsonify(resp_data)


@csrf_protect.exempt
@blueprint.route('/register', methods=["GET", "POST"])
def register_html():
    """
    注册页面
    :return:
    """
    logging.info('用户注册')
    logout_user()  # 清除用户信息
    session.clear()  # 清除session
    form = RegisterForm()
    return render_template('register.html', form=form)


@csrf_protect.exempt
@blueprint.route('/register/user', methods=['POST'])
def register_user():
    """
    用户注册
    :return:
    """
    logging.info('register_user')
    resp_data = {}
    try:

        form = RegisterForm()
        params = request.get_json()
        if form.validate_on_submit():
            # 创建新用户
            User.create(email=params.get('email'), password=params.get('password'))
            resp_data["code"] = response.SUCCESS
            resp_data["msg"] = response.RESULT_SUCCESS
            resp_data["data"] = []
        else:
            resp_data["code"] = response.PARAMETER_ERROR
            resp_data["msg"] = response.RESULT_PARAMETER_ERROR
            resp_data["data"] = {'password': form.password.errors}
    except Exception as e:
        logging.error(e)
        resp_data["code"] = response.ERROR
        resp_data["msg"] = []
        resp_data["data"] = response.RESULT_ERROR
    finally:
        return jsonify(resp_data)
































