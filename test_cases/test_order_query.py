import os

import allure
import pytest

import config
from apis.order_query_api import OrderQueryApi
from utils.assert_result import AssertResult
from utils.read_excel import ReadExcel

datas = ReadExcel.read_excel(os.path.join(config.datas_path,'auto.xlsx'), 'orderquery')


@allure.feature("搜索模块")
@allure.story("搜索功能")
class TestOrderQuery:

    @pytest.mark.parametrize("title,order_data,status_code,code,msg",datas)
    @allure.title("{title}")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_success(self,title,order_data,status_code,code,msg,get_logger,login):
        get_logger.info(f"开始执行用例：{title}")
        with allure.step("登录"):
            res = OrderQueryApi.order_query(login,order_data)
        get_logger.info(res.text)
        with allure.step("断言结果"):
            AssertResult.assert_result(res,status_code,code,msg)