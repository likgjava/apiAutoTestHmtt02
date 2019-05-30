import app
import requests


# 自媒体
class MpLoginApi:
    def __init__(self):
        self.login_url = app.BASE_URL_MP + "/authorizations"

    def login(self, mobile, code):
        param = {"mobile": mobile, "code": code}
        return requests.post(self.login_url, json=param, headers=app.headers_data_mp)


# 后台管理系统
class MisLoginApi:
    def __init__(self):
        self.login_url = app.BASE_URL_MIS + "/authorizations"

    def login(self, account, pwd):
        param = {"account": account, "password": pwd}
        return requests.post(self.login_url, json=param, headers=app.headers_data_mis)


# APP
class AppLoginApi:
    def __init__(self):
        self.login_url = app.BASE_URL_APP + "/authorizations"

    def login(self, mobile, code):
        param = {"mobile": mobile, "code": code}
        return requests.post(self.login_url, json=param, headers=app.headers_data_app)
