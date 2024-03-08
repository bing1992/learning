import re
from pathlib import Path

import jsonpath
import pytest
import requests

from commons.request_util import RequestUtil
from commons.yaml_extract_util import write_extract_yaml, read_extract_yaml, read_product_yaml

# from testcases.usermanager.test_apis import TestApi2

test_path = str(Path(__file__).parent)


class TestShopxo:

    # token = ""

    # 测试首页接口
    @pytest.mark.parametrize("caseinfo", read_product_yaml(test_path+"/test_index.yaml"))
    def test_index(self, caseinfo):
        url = caseinfo["request"]["url"]
        method = caseinfo["request"]["method"]
        params = caseinfo["request"]["params"]
        res = RequestUtil(caseinfo).send_all_request(method=method, url=url, params=params)
        print(res.json())

    @pytest.mark.parametrize("caseinfo", read_product_yaml(test_path + "/test_product_detail.yaml"))
    def test_product_detail(self,caseinfo):
        url = caseinfo["request"]["url"]
        method = caseinfo["request"]["method"]
        params = caseinfo["request"]["params"]
        json = caseinfo["request"]["json"]
        res = RequestUtil(caseinfo).send_all_request(method=method, url=url, params=params, json=json)
        print(caseinfo)

    @pytest.mark.parametrize("caseinfo", read_product_yaml(test_path + "/test_login.yaml"))
    def test_login(self, caseinfo):
        url = caseinfo["request"]["url"]
        method = caseinfo["request"]["method"]
        params = caseinfo["request"]["params"]
        json = caseinfo["request"]["json"]
        res = RequestUtil(caseinfo).send_all_request(method=method, url=url, params=params, json=json)
        print(res.json())
        token_data = {"token": res.json()["data"]["token"]}
        write_extract_yaml("./extract.yaml", token_data)

        print(token_data)

    @pytest.mark.parametrize("caseinfo", read_product_yaml(test_path + "/test_order.yaml"))
    def test_order_detail(self,caseinfo):
        params = {
            "token": read_extract_yaml("./extract.yaml", "token")
        }
        url = caseinfo["request"]["url"]
        method = caseinfo["request"]["method"]
        yaml_params = caseinfo["request"]["params"]
        params.update(yaml_params)
        json = caseinfo["request"]["json"]
        res = RequestUtil(caseinfo).send_all_request(method=method, url=url, params=params, json=json)
        print(res.json())