import pytest


def clear_extract_yaml():
    with open("./extract.yaml", encoding="utf-8", mode="w") as f:
        pass


@pytest.fixture(scope="session", autouse=True)
def auto_clear_extract_yaml():
    clear_extract_yaml()