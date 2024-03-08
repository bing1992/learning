import yaml


# 读取
def read_extract_yaml(yaml_path, key):
    with open(yaml_path, encoding="utf-8") as f:
        # value = yaml.load(f, Loader=yaml.FullLoader)
        value = yaml.safe_load(f)
        return value[key]


# 写入
def write_extract_yaml(yaml_path, data):
    with open(yaml_path, encoding='utf-8', mode='a+') as f:
        # yaml.dump(data, stream=f, allow_unicode=True)
        yaml.safe_dump(data, stream=f, allow_unicode=True)


def read_product_yaml(yaml_path):
    with open(yaml_path, encoding="utf-8") as f:
        value = yaml.safe_load(f)
        return value

# 清空
# def clear_extract_yaml(yaml_path):
#     with open(yaml_path, encoding='utf-8', mode='w') as f:
#         # f.truncate()
#         pass
