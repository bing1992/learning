import requests

from commons.models import verify_yaml


class RequestUtil:

    session = requests.session()

    def __init__(self, case):
        self.case = case

    def send_all_request(self, **kwargs):
        # 公共参数：
        params = {
            "application": "app",
            "application_client_type": "h5"
        }
        for args_key, args_value in kwargs.items():
            if args_key == "params":
                kwargs["params"].update(params)
        verify_yaml(self.case)
        res = RequestUtil.session.request(**kwargs)
        return res


