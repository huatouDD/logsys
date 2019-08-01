from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_logconfig import LogConfig
from flask_security import Security
from flask_security.core import LoginManager
from flask_wtf.csrf import CsrfProtect

security = Security()
login_manager = LoginManager()
bcrypt = Bcrypt()
db = MongoEngine()
logcfg = LogConfig()  # LOG
csrf_protect = CsrfProtect()  # csrf保护
login_manager.session_protection = None

login_manager.login_view = "/login/"
