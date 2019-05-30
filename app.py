import logging.handlers
import os

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 自媒体系统的基础URL
BASE_URL_MP = "http://ttapi.research.itcast.cn/mp/v1_0"
BASE_URL_MIS = "http://ttapi.research.itcast.cn/mis/v1_0"
BASE_URL_APP = "http://ttapi.research.itcast.cn/app/v1_0"
BASE_URL_APP_V1_1 = "http://ttapi.research.itcast.cn/app/v1_1"

# 存放请求头数据
headers_data_mp = {
    "Content-Type": "application/json",
    # "Authorization": "xxx"
}
headers_data_mis = {
    "Content-Type": "application/json",
}
headers_data_app = {
    "Content-Type": "application/json",
}


# 初始化日志配置
def init_log_config():
    # 创建日志器对象
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 创建处理器
    sh = logging.StreamHandler()
    fh = logging.handlers.TimedRotatingFileHandler(BASE_DIR + "/log/hmtt.log", when="midnight", interval=1,
                                                   backupCount=7, encoding="UTF-8")

    # 创建格式化器
    fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)

    # 把格式化器添加到处理器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 把处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)
