from flask import Blueprint

blueprint = Blueprint('users', __name__, static_folder='../static')
