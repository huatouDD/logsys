import datetime
import time

from logsys.extensions import db


def create_data_id(prefix):
    base_str = str(time.time()).replace('.', '')[:13]
    return prefix + '{:0<13}'.format(base_str)


class LoggingData(db.Document):
    data_id = db.StringField()  # 数据唯一标识
    log_data = db.StringField()  # 存放数据
    create_time = db.DateTimeField()  # 更新时间

    @classmethod
    def create_data(cls, **kwargs):
        try:
            info = cls(
                data_id=create_data_id('log'),
                log_data=kwargs.get('log_data'),
                create_time=datetime.datetime.now()
            )
            info.save()
            return info
        except Exception as e:
            raise e
