import yaml


class YamlUtil():
    def __init__(self, yaml_path):
        self.yaml_path = yaml_path

    # 读取
    def read_yaml(self):
        with open(self.yaml_path, encoding="utf-8") as f:
            # value = yaml.load(f, Loader=yaml.FullLoader)
            value = yaml.safe_load(f)
            return value

    # 写入
    def write_yaml(self, data):
        with open(self.yaml_path, encoding='utf-8', mode='w') as f:
            # yaml.dump(data, stream=f, allow_unicode=True)
            yaml.safe_dump(data, stream=f, allow_unicode=True)

    # 清空
    def clear_yaml(self):
        with open(self.yaml_path, encoding='utf-8', mode='w') as f:
            f.truncate()
