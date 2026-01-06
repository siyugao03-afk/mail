import requests

from config import project_url


class LoginApi:
    @classmethod
    def login(cls,login_data):
        login_url =project_url+"/login"
        res = requests.post(login_url,json=login_data)
        return res