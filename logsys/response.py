"""
请求码
"""

SUCCESS = "0"  # 成功
ERROR = '-1'  # 请求异常
PARAMETER_ERROR = '-2'  # 参数错误
UN_AUTH_ERROR = "-4"  # auth_token认证失败

"""
请求结果
"""

RESULT_SUCCESS = '请求成功'
RESULT_ERROR = '请求失败'
RESULT_PARAMETER_ERROR = '参数错误'
RESULT_PERMISSION_ERROR = '暂无权限'
RESULT_EXIT_ERROR = '对象已存在'
RESULT_UN_AUTH_ERROR = '认证失败, 请重新登录'
