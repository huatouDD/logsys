from flask import Blueprint, render_template

from logsys.data.models import LoggingData
from logsys.users.models import User

blueprint = Blueprint('log_data', __name__, static_folder='../static')


@blueprint.route('/test', methods=["GET"])
def index():
    """
    test
    :return:
    """
    info = LoggingData.create_data(log_data="123123123")
    user = User()
    user.create(email='huatoudd@163.com', password='1254156415')
    return render_template('index.html', info=info, user=user)
