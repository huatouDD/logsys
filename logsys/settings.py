import datetime
import os


class Config:
    DEBUG = False
    # 随机生成
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = True


    # SECURITY_LOGIN_URL = '/login/'  # 登录端口/
    SECURITY_POST_LOGIN_VIEW = '/'  # 指定用户登录后默认跳转的页面
    # flask-security消息文本
    SECURITY_MSG_USER_DOES_NOT_EXIST = ['用户名错误', '']  # 登陆时用户名错误提醒
    SECURITY_MSG_INVALID_PASSWORD = ['密码错误', '']  # 登陆时密码错误提醒
    # 创建redis数据库的连接，并把session存入redis中
    # REDIS_HOST = '127.0.0.1'
    # REDIS_PORT = 6379

    # StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置SESSION中的属性
    # SEESION_TYPE = 'redis'
    # SESSION_USE_SIGNER = True
    # PERMANENT_SESSION_LIFETIME = 84600

    # 指定日志的格式，按照每天一个日志文件的方式
    LOG_FILE = './logs/{0}-{1}.log'.format('logSys', datetime.datetime.now().strftime("%Y-%m-%d"))
    LOGCONFIG = {
        'version': 1,
        'disable_existing_loggers': False,

        'filters': {
            'require_debug_false': {
                '()': 'logsys.logging.log.RequestFilter'
            }
        },
        'formatters': {
            'simple': {
                'format': '[%(levelname)s] %(module)s : %(message)s'
            },
            'verbose': {
                'format':
                    '[%(asctime)s] [%(levelname)s] %(module)s : %(message)s'
            }
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',  # TODO
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            },
            'file': {
                'level': 'DEBUG',  # TODO
                'class': 'logging.FileHandler',
                'formatter': 'verbose',
                'filename': LOG_FILE,
                'mode': 'a',
            },
        },
        'loggers': {
            '': {
                'handlers': ['file', 'console'],
                'level': 'DEBUG',
                'propagate': True,
            },
        }
    }


class DevConfig(Config):
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False  # 拦截重定向
    # mongodb并不是进程安全的，在多进程下，connect设置为false
    # MONGODB_SETTINGS = {'db': 'logSys', 'host': '172.16.222.132', 'port': 27017, 'connect': False, 'username': 'sa',
    #                     'password': 'mongodba'}
    MONGODB_SETTINGS = {'db': 'logSys', 'host': '172.16.222.132', 'port': 27017}


class ProdConfig(Config):
    DEBUG = False
