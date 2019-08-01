from flask_security import UserMixin, RoleMixin
from werkzeug.security import generate_password_hash, check_password_hash
from logsys.extensions import db


class Role(db.Document, RoleMixin):
    mete = {
        'collection': 'role'
    }
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)


class User(db.Document, UserMixin):
    meta = {
        'collection': 'user'
    }
    email = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    roles = db.ListField(db.ReferenceField(Role), default=[])

    # 账号密码
    @property
    def _password(self):
        return self.password

    @_password.setter
    def _password(self, password):
        self.password = generate_password_hash(password)
        self.save()

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def create(cls, **kwargs):
        """
        创建新用户
        :return:
        """
        user = User()
        user._password = kwargs.get('password')
        user.email = kwargs.get('email')
        user.save()
        return None
