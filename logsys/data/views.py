from flask import Blueprint, render_template
from flask_login import login_required

from logsys.data.models import LoggingData
from logsys.users.models import User

blueprint = Blueprint('log_data', __name__, static_folder='../static')


@blueprint.route('/test', methods=["GET"])
def test():
    """
    test
    :return:
    """
    info = LoggingData.create_data(log_data="123123123")
    user = User()
    user.create(email='huatoudd@163.com', password='123456')
    return render_template('index.html', info=info, user=user)

#
@blueprint.route('/index', methods=["GET"])
@login_required
def index():
    """
    test
    :return:
    """
    return render_template('login_success.html')
