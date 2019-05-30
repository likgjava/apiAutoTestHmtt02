import json

import app
import utils
from api import ApiFactory
import pytest
import logging


# 自媒体-登录-构建测试数据
def build_data_mp_login():
    test_data = []
    with open(app.BASE_DIR + "/data/publish.json", encoding="UTF-8") as f:
        data = json.load(f)
        case_data = data.get("test_mp_login")
        test_data.append((case_data.get("mobile"), case_data.get("code")))
    logging.info("test_data={}".format(test_data))
    return test_data


class TestPublishProcess:
    title = "test115"
    article_id = None
    channel_id = 1

    # 自媒体-登录
    @pytest.mark.parametrize("mobile,code", build_data_mp_login())
    def test_mp_login(self, mobile, code):
        logging.info("mobile={} code={}".format(mobile, code))
        # 测试数据
        # mobile = "13911111111"
        # code = "123456"

        # 调用登录接口
        response = ApiFactory.mp_login_api.login(mobile, code)
        logging.info("json data={}".format(response.json()))

        # 断言
        utils.common_assert(response, 201)

        # 保存token数据
        app.headers_data_mp["Authorization"] = "Bearer " + response.json().get("data").get("token")
        logging.info("headers_data_mp={}".format(app.headers_data_mp))

    # 自媒体-发布文章
    def test_mp_publish_article(self):
        logging.info("test_mp_publish_article start.....")
        # 测试数据
        content = "今天天气不错，心情很美丽！！！"
        channel_id = TestPublishProcess.channel_id
        cover_type = 0

        # 发布文章
        response = ApiFactory.mp_article_api.publish_article(TestPublishProcess.title, content, channel_id, cover_type)
        print("json data=", response.json())

        # 断言
        utils.common_assert(response, 201)

    # 后台-登录
    def test_mis_login(self):
        # 测试数据
        account = "testid"
        pwd = "testpwd123"

        # 登录
        response = ApiFactory.mis_login_api.login(account, pwd)

        # 断言
        utils.common_assert(response, 201)

        # 保存token数据
        app.headers_data_mis["Authorization"] = "Bearer " + response.json().get("data").get("token")
        print("headers_data_mis=", app.headers_data_mis)

    # 后台-查询文章
    def test_mis_query_article(self):
        # 测试数据
        title = TestPublishProcess.title
        channel = "html"

        # 查询
        response = ApiFactory.mis_article_api.query_articles(title, channel)

        # 断言
        utils.common_assert(response, 200)
        articles = response.json().get("data").get("articles")
        print("articles==", articles)
        assert title == articles[0].get("title")

        # 保存文章ID
        TestPublishProcess.article_id = articles[0].get("article_id")
        print("TestPublishProcess.article_id=", TestPublishProcess.article_id)

    # 后台-审核文章
    def test_mis_audit_article(self):
        # 测试数据
        article_id = TestPublishProcess.article_id
        # status = 2  # 审核通过
        status = 4  # 删除文章

        # 审核
        response = ApiFactory.mis_article_api.audit_article(article_id, status)
        print("json data=", response.json())

        # 断言
        utils.common_assert(response, 201)

    # APP-登录
    def test_app_login(self):
        # 测试数据
        mobile = "13911111111"
        code = "123456"

        # 登录
        response = ApiFactory.app_login_api.login(mobile, code)
        print("json data=", response.json())

        # 断言
        utils.common_assert(response, 201)

        # 保存token数据
        app.headers_data_app["Authorization"] = "Bearer " + response.json().get("data").get("token")
        print("headers_data_app=", app.headers_data_app)

    # APP-获取文章列表
    def test_get_articles(self):
        # 测试数据
        channel_id = TestPublishProcess.channel_id

        # 查询文章
        response = ApiFactory.app_article_api.get_articles(channel_id)
        print("json data=", response.json())

        # 断言
        utils.common_assert(response, 200)
