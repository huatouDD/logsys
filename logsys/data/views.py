from flask import Blueprint, render_template

from logsys.data.models import LoggingData

blueprint = Blueprint('log_data', __name__, static_folder='../static')


@blueprint.route('/', methods=["GET"])
def index():
    """
    test
    :return:
    """
    info = LoggingData.create_data(log_data="123123123")
    return render_template('index.html', info=info)
