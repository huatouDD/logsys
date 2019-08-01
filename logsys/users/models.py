from flask_security import UserMixin, RoleMixin
from werkzeug.security import generate_password_hash, check_password_hash

from logsys.extensions import db
from flask_security.utils import hash_password, verify_password


# class User(db.Document):
#     meta = {
#         'collection': 'users'
#     }
#     user_code = db.StringField()
#     name = db.StringField(max_length=255, required=False)   # 用户名
#     email = db.StringField(max_length=80)   # 用户邮箱
#     password = db.StringField(max_length=255)   # 密码哈希值
#
#     @property       # gettr
#     def _password(self):
#         return self.password
#
#     @_password.setter   # setter
#     def _password(self, password):
#         self.password = hash_password(password)


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

    def set_password(self, password):
        """
        注册加密
        :param password:
        :return:
        """
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """
        校验解密
        :param password:
        :return:
        """
        return check_password_hash(self.password, password)

    def create(self, **kwargs):
        """
        创建新用户
        :return:
        """
        self.set_password(kwargs.get('password'))
        self.email = kwargs.get('email')
        self.save()

