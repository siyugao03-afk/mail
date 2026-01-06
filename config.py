#工程路径
import os.path

project_path = os.path.dirname(os.path.abspath(__file__))
datas_path = os.path.join(project_path, 'datas')
logs_path = os.path.join(project_path, 'logs')
#项目路径
project_url = 'https://admin-api.macrozheng.com/admin'

if __name__ == '__main__':
    print(os.path.dirname(os.path.abspath(__file__)))
    print(datas_path)