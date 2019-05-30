import app
from api.article import MpArticleApi, MisArticleApi, AppArticleApi
from api.login import MpLoginApi, MisLoginApi, AppLoginApi

# 初始化日志配置
app.init_log_config()


# 获取接口类对象的工厂
class ApiFactory:
    # 自媒体-登录
    mp_login_api = MpLoginApi()
    # 自媒体-文章
    mp_article_api = MpArticleApi()
    # 后台-登录
    mis_login_api = MisLoginApi()
    # 后台- 文章
    mis_article_api = MisArticleApi()
    # APP-登录
    app_login_api = AppLoginApi()
    # APP-文章
    app_article_api = AppArticleApi()
