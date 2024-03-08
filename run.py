import pytest
import time
import os

import requests

if __name__ == '__main__':
    pytest.main(["-vs"])
    time.sleep(3)
    os.system("allure generate ./temps -o ./reports --clean")

    proxies = {
            "http": "http://127.0.0.1:8888"
        }
    # data = {
    #     "name1": "百里",
    #     "name2": "天球"
    # }
    # filedata = {
    #     "uploadfile": ("shu.jpg", "百里老师", "image/jpeg"),
    #     "filename": open("D:\\shu.jpg", "rb")
    # }
    # res = requests.post(url="http://47.107.116.139/phpwind/")
    # # print(res.status_code)
    # # print(res.reason)
    # # print(res.encoding)
    # # print(res.cookies)
    # print(res.headers)
    # print(res.elapsed)
    # print(res.text)
    # print(res.content)