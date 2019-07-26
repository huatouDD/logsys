from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_logconfig import LogConfig
from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect

login_manager = LoginManager()
bcrypt = Bcrypt()
db = MongoEngine()
logcfg = LogConfig()  # LOG
csrf_protect = CsrfProtect()  # csrf保护
login_manager.session_protection = None
