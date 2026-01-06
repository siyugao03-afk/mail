import os

import openpyxl

from config import datas_path


class ReadExcel:
    @staticmethod
    def read_excel(file_path,sheet_name):
        datas = []
        try:
            wk = openpyxl.load_workbook(file_path)
            sheet = wk[sheet_name]
            for row in sheet.iter_rows(min_row=2):
                data = tuple([cell.value for cell in row])
                datas.append(data)
        except Exception as e:
            print(e)
        print(datas)
        return datas

if __name__ == '__main__':
   ReadExcel.read_excel(os.path.join(datas_path,'auto.xlsx'), 'mail_login')