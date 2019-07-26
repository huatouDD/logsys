from flask import Flask

from logsys import data
from logsys.extensions import logcfg, db, csrf_protect, bcrypt, login_manager
from logsys.settings import DevConfig
from flask_wtf import csrf


# 工厂函数
def create_app(config_object=DevConfig):
    app = Flask(__name__)
    # 导入settings文件
    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)

    return app


# 注册蓝图
def register_blueprints(app):
    app.register_blueprint(data.views.blueprint)
    return None


# 第三方插件
def register_extensions(app):
    login_manager.init_app(app)
    bcrypt.init_app(app)
    logcfg.init_app(app)  # log配置信息
    db.init_app(app)
    csrf_protect.init_app(app)
    return None


