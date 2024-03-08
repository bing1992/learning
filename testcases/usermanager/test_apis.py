import time
import json
import re
from pathlib import Path

import jsonpath as jsonpath
import pytest
import allure
# from commons import yaml_util
import requests

from commons.request_util import RequestUtil
from commons.yaml_extract_util import write_extract_yaml, read_extract_yaml, read_product_yaml

# from commons.yaml_util import  YamlUtil

test_path = str(Path(__file__).parent)

class TestApi2:

    session = requests.session()
    # access_token = ""
    # csrf_token = ""
    # cookies = ""

    @pytest.mark.parametrize("caseinfo", read_product_yaml(test_path+"/test_phpwind_start.yaml"))
    def test_phpwind_start(self, caseinfo):
        url = caseinfo["request"]["url"]
        method = caseinfo['request']['method']
        res = RequestUtil(caseinfo).send_all_request(method=method, url=url)
        value = re.findall('name="csrf_token" value="(.*?)"', res.text)
        print(value[0])
        csrf_token_data = {"csrf_token": value[0]}
        write_extract_yaml("./extract.yaml", csrf_token_data)

    @pytest.mark.parametrize("caseinfo", read_product_yaml(test_path + "/test_phpwind_login.yaml"))
    def test_phpwind_login(self, caseinfo):
        url = caseinfo["request"]["url"]
        method = caseinfo['request']['method']
        headers = caseinfo['request']['headers']
        data = caseinfo['request']['data']
        data["csrf_token"] = read_extract_yaml("./extract.yaml", "csrf_token")
        res = RequestUtil(caseinfo).send_all_request(method=method, url=url, headers=headers, data=data)
        print(res.json())

    @pytest.mark.parametrize("caseinfo", read_product_yaml(test_path + "/test_get_token.yaml"))
    def test_get_token(self,caseinfo):
        url = caseinfo["request"]["url"]
        method = caseinfo['request']['method']
        params = caseinfo['request']['params']
        res = RequestUtil(caseinfo).send_all_request(method=method, url=url, params=params)
        print(res.json())
        value = jsonpath.jsonpath(res.json(), "$.access_token")
        access_token_data = {"access_token": value[0]}
        write_extract_yaml("./extract.yaml", access_token_data)

    # def test_create_flag(self):
    #     params = {
    #         "access_token": read_extract_yaml("./extract.yaml", "access_token")
    #     }
    #     json = {
    #         "tag": {"name": f"广东人{str(int(time.time()))}"}
    #     }
    #     res = RequestUtil().send_all_request(method="post", url="https://api.weixin.qq.com/cgi-bin/tags/create",
    #                         params=params,
    #                         json=json)
    #     print(res.json())
    @pytest.mark.parametrize("caseinfo", read_product_yaml(test_path + "/test_get_flag.yaml"))
    def test_get_flag(self, caseinfo):
        url = caseinfo["request"]["url"]
        method = caseinfo['request']['method']
        params = caseinfo['request']['params']
        params["access_token"] = read_extract_yaml("./extract.yaml", "access_token")
        res = RequestUtil(caseinfo).send_all_request(method=method, url=url, params=params)
        print(res.json())

    @pytest.mark.parametrize("caseinfo", read_product_yaml(test_path + "/test_delete_flag.yaml"))
    def test_delete_flag(self, caseinfo):
        url = caseinfo["request"]["url"]
        method = caseinfo['request']['method']
        params = caseinfo['request']['params']
        json = caseinfo['request']['json']
        params["access_token"] = read_extract_yaml("./extract.yaml", "access_token")
        # params = {
        #     "access_token": read_extract_yaml("./extract.yaml", "access_token")
        # }
        # json = {
        #     "tag": {"id": 172}
        # }
        res = RequestUtil(caseinfo).send_all_request(method=method, url=url, params=params, json=json)
        print(res.json())


