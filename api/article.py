import time

import app
import requests


# 自媒体-文章
class MpArticleApi:
    def __init__(self):
        # 发布文章
        self.publish_article_url = app.BASE_URL_MP + "/articles"

    def publish_article(self, title, content, channel_id, cover_type):
        param = {
            "title": title,
            "content": content,
            "channel_id": channel_id,
            "cover": {"type": cover_type, "images": []}
        }
        return requests.post(self.publish_article_url, json=param, headers=app.headers_data_mp)


# 后台-文章
class MisArticleApi:
    def __init__(self):
        # 查询文章列表
        self.query_articles_url = app.BASE_URL_MIS + "/articles"
        # 审核文章
        self.audit_article_url = app.BASE_URL_MIS + "/articles"

    # 查询文章列表
    def query_articles(self, title, channel):
        query_string = {
            "title": title,
            "channel": channel
        }
        return requests.get(self.query_articles_url, params=query_string, headers=app.headers_data_mis)

    # 审核文章
    def audit_article(self, article_id, status):
        param = {"article_ids": [article_id], "status": status}
        return requests.put(self.audit_article_url, json=param, headers=app.headers_data_mis)


# APP-文章
class AppArticleApi:
    def __init__(self):
        self.articles_url = app.BASE_URL_APP_V1_1 + "/articles"

    # 获取文章列表
    def get_articles(self, channel_id):
        # channel_id=1&timestamp=1222333&with_top=1
        query_string = {
            "channel_id": channel_id,
            "timestamp": int(time.time() * 1000),
            "with_top": 1
        }
        return requests.get(self.articles_url, params=query_string, headers=app.headers_data_app)
