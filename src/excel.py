import platform
import os
import openpyxl
import pandas as pd
import subprocess
from typing import List
from openpyxl.styles.borders import Border, Side
from openpyxl.styles.fonts import Font
from openpyxl.utils import get_column_letter
from openpyxl.drawing.image import Image
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.worksheet.cell_range import CellRange

from get_paths import get_excel_output_path, get_format_excel_fullpath


class Excel:

    def __init__(self)->None:

        self.cols_dic: dict = {
            'STAN_COL_last26Deli_to_this25Deli': 2, 
            'STAN_COL_this1Deli_to_this25Deli': 3, 
            'STAN_COL_this26Deli_to_thisEndDeli': 4, 
            'STAN_COL_last26Deli_to_lastEndDeli': 5, 
            'TOYO_COL_last26Deli_to_this25Deli': 8, 
            'TOYO_COL_this1Deli_to_this25Deli': 9, 
            'TOYO_COL_this26Deli_to_thisEndDeli': 10,
            'TOYO_COL_last26Deli_to_lastEndDeli': 11,
            'TOYO_COL_lastShip_to_thisDeli': 12,
            'TOYO_COL_this1Ship_to_this25Deli': 13
        }

        self.rows_dic: dict = {
            'ROW_HADANO': 3,
            'ROW_HAMAMATSU': 4,
            'ROW_OKAZAKI': 5,
            'ROW_HIROSHIMA': 6,
            'ROW_KUMAMOTO': 7,
            'ROW_TOTAL': 8,
            'ROW_TAX': 9,
            'ROW_AMOUNT_INCLUDING_TAX': 10
        }

        format_fullpath: str = get_format_excel_fullpath()
        self.wb:openpyxl.Workbook = openpyxl.load_workbook(
                filename= format_fullpath, data_only=True)
        self.ws:Worksheet = self.wb['kensyu']


    def write_uri_mount_to_ws_toyo(self, mukesaki: str, period: str,
                              uri_amount: int) -> None:
        row: int = self.rows_dic[f'ROW_{mukesaki.upper()}']
        col: int = self.cols_dic[f'TOYO_COL_{period}']
        self.ws.cell(row=row, column=col, value=uri_amount)


    def write_uri_total_to_ws_toyo(self, period: str,
                              uri_total: int) -> None:
        row: int = self.rows_dic['ROW_TOTAL']
        col: int = self.cols_dic[f'TOYO_COL_{period}']
        self.ws.cell(row=row, column=col, value=uri_total)
        

    def write_uri_mount_to_ws_stan(self, mukesaki: str, period: str,
                              uri_amount: int) -> None:
        row: int = self.rows_dic[f'ROW_{mukesaki.upper()}']
        col: int = self.cols_dic[f'STAN_COL_{period}']
        self.ws.cell(row=row, column=col, value=uri_amount)


    def write_uri_total_to_ws_stan(self, period: str,
                              uri_total: int) -> None:
        row: int = self.rows_dic['ROW_TOTAL']
        col: int = self.cols_dic[f'STAN_COL_{period}']
        self.ws.cell(row=row, column=col, value=uri_total)
        

    def write_tax_total_to_ws_stan(self, period: str,
                              tax_total: int) -> None:
        row: int = self.rows_dic['ROW_TAX']
        col: int = self.cols_dic[f'STAN_COL_{period}']
        self.ws.cell(row=row, column=col, value=tax_total)
        

    def save_file(self)->None:
        output_path: str = get_excel_output_path()
        try:
            self.wb.save(filename= f'{output_path}out.xlsx')
        except Exception:
            print('ファイルを保存できません。record_sheet.xlsxを閉じてください')

