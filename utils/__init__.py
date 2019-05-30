# 通用的断言方法
def common_assert(response, status_code=200, message="OK"):
    # 断言响应状态码
    assert response.status_code == status_code
    # 断言响应消息
    assert response.json().get("message") == message
