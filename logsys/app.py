import logging

from flask import Flask, request, jsonify, redirect
from flask_security.datastore import MongoEngineUserDatastore
from werkzeug.security import generate_password_hash

from logsys import data, users, response, public
from logsys.extensions import logcfg, db, csrf_protect, bcrypt, login_manager, security
from logsys.public.forms import LoginForm
from logsys.settings import DevConfig

user_datastore = MongoEngineUserDatastore(db, users.models.User, users.models.Role)


# 工厂函数
def create_app(config_object=DevConfig):
    app = Flask(__name__)
    # 导入settings文件
    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)
    #
    # @app.before_first_request
    # def create_user_first():
    #     """
    #     生成第一个用户
    #     :return:
    #     """
    #     user_datastore.create_user(email='444398404@qq.com', password_hash=generate_password_hash('wujiehua'))
    return app


# 注册蓝图
def register_blueprints(app):
    app.register_blueprint(data.views.blueprint)
    app.register_blueprint(public.views.blueprint)
    return None


# 第三方插件
def register_extensions(app):
    bcrypt.init_app(app)
    logcfg.init_app(app)  # log配置信息
    db.init_app(app)
    csrf_protect.init_app(app)
    login_manager.init_app(app)
    security.init_app(app, user_datastore).unauthorized_handler(un_auth_handler)
    return None


def un_auth_handler():
    """
    auth_token认证失败回调
    :return:
    """
    logging.info('认证失败')
    if request.method == 'POST':
        return jsonify({
            'code': response.UN_AUTH_ERROR,
            'data': "",
            'msg': response.RESULT_UN_AUTH_ERROR
        })

    else:
        return redirect("/login/")
