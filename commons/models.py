from dataclasses import dataclass
# 自动传参和自动校验的工具类
import yaml


@dataclass
class CaseInfo:
    # 必填
    feature: str
    story: str
    title: str
    request: dict
    validate: dict
    # 选填
    extract: dict = None
    parameties: list = None


def verify_yaml(caseinfo: dict):
    try:
        new_case = CaseInfo(**caseinfo)
        print(new_case)
        return new_case
    except Exception:
        raise Exception("YAML文件不符合要求")
        # print("YAML文件不符合要求")


if __name__ == '__main__':
    with open(r"D:\桌面\7月找工作\04-pytest\api_frame_231\testcases\shopxomanager\test_index.yaml", encoding='utf-8') as f:
        yaml_dict = yaml.safe_load(f)
        print(*yaml_dict)
        verify_yaml(*yaml_dict)