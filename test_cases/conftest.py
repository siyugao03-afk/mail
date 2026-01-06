import pytest

from apis.login_api import LoginApi
from utils.log_util import LogUtil


@pytest.fixture(scope="function")
def login():
    login_data = {"username": "admin", "password": "macro123"}
    res = LoginApi.login(login_data)
    token = res.json().get('data').get('token')
    yield token

@pytest.fixture(scope="class")
def get_logger():
    logger = LogUtil.get_logger()
    yield logger