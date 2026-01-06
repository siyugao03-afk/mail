import requests

from config import project_url


class OrderQueryApi:
    @classmethod
    def order_query(cls,token,order_data):
        order_query_url =project_url+"/list?pageNum=1&pageSize=10&keyword=订单"
        headers_data = {"authorization":"Bearer"+" "+token}
        res = requests.post(order_query_url,json=order_data,headers=headers_data)
        return res