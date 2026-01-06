import os

import allure
import pytest

import config
from apis.login_api import LoginApi
from test_cases.conftest import get_logger
from utils.assert_result import AssertResult
from utils.read_excel import ReadExcel

datas = ReadExcel.read_excel(os.path.join(config.datas_path,'auto.xlsx'), 'mail_login')
@allure.feature("登录模块")
@allure.story("登录功能")
class TestLogin:

    @pytest.mark.parametrize("title,login_data,status_code,code,msg",datas)
    @allure.title("{title}")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_success(self,title,login_data,status_code,code,msg,get_logger):
        get_logger.info(f"开始执行用例：{title}")
        with allure.step("登录"):
            res = LoginApi.login(login_data)
        get_logger.info(res.text)
        with allure.step("断言结果"):
            AssertResult.assert_result(res,status_code,code,msg)
