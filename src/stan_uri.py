from i_uri_data import IUriData
from typing import Dict, List, Any
from get_idx import GetIdx

class StanUri(IUriData):
    '''
    col = ['order_no', 'tokui_name', 'hinban', 'amount',
           'deli_day', 'tanka', 'qty', 'tax']
    uri_dataが無い場合は空のリストが渡ってくる[]

    '''
    def __init__(self, uri_data: List[Any], mukesaki: str,
                 uri_col: List[str], dates_dic:Dict[str, str]) -> None:

        # メンバ変数の初期化　uri_dataが空のリストの場合は、各変数は初期値のまま
        self._dates_dic = dates_dic
        self._mukesaki= mukesaki # hadanoなど 
        self._order_no: str = ''
        self._tokui_name: str = ''
        self._hinban: str = ''
        self._amount: int = 0
        self._deli_day: str = ''
        self._tanka: int = 0
        self._qty: int = 0
        self._tax: int = 0

        order_no_idx: int = GetIdx.get_idx(uri_col, 'order_no')
        tokui_name_idx: int = GetIdx.get_idx(uri_col, 'tokui_name')
        hinban_idx: int = GetIdx.get_idx(uri_col, 'hinban')
        amount_idx: int = GetIdx.get_idx(uri_col, 'amount')
        deli_day_idx: int = GetIdx.get_idx(uri_col, 'deli_day')
        tanka_idx: int = GetIdx.get_idx(uri_col, 'tanka')
        qty_idx: int = GetIdx.get_idx(uri_col, 'qty')
        tax_idx: int = GetIdx.get_idx(uri_col, 'tax')


        if uri_data:
            self._order_no: str = uri_data[order_no_idx]
            self._tokui_name: str = uri_data[tokui_name_idx]
            self._hinban: str = uri_data[hinban_idx]
            self._amount: int = int(uri_data[amount_idx])
            self._deli_day: str = uri_data[deli_day_idx]
            self._tanka: int = int(uri_data[tanka_idx])
            self._qty: int = int(uri_data[qty_idx])
            self._tax: int = int(uri_data[tax_idx])


    def add_amount(self, mukesaki: str, period: str, 
                   sum_amount: int, uri_or_tax = 'uri')-> int:

        if self._mukesaki != mukesaki:
            return sum_amount + 0

        last1: str = self._dates_dic['last_month'] + '01'
        last26: str = self._dates_dic['last_month'] + '26'
        lastEnd: str = self._dates_dic['last_month_end']
        this1: str = self._dates_dic['this_month'] + '01'
        this25: str = self._dates_dic['this_month'] + '25'
        this26: str = self._dates_dic['this_month'] + '26'
        thisEnd: str = self._dates_dic['this_month_end']

        if period == 'last26Deli_to_this25Deli':
            sum_amount = self._add_last26Deli_to_this25Deli(
                    sum_amount, last26, this25, uri_or_tax
            )
        if period == 'this1Deli_to_this25Deli':
            sum_amount = self._add_this1Deli_to_this25Deli(
                    sum_amount, this1, this25, uri_or_tax
            )
        if period == 'this26Deli_to_thisEndDeli':
            sum_amount = self._add_this26Deli_to_thisEndDeli(
                    sum_amount, this26, thisEnd, uri_or_tax
            )
        if period == 'last26Deli_to_lastEndDeli':
            sum_amount = self._add_last26Deli_to_lastEndDeli(
                    sum_amount, last26, lastEnd, uri_or_tax
            )

        return sum_amount

    def _add_last26Deli_to_this25Deli(self, sum_amount: int, 
                                      stt_day: str, end_day: str,
                                      uri_or_tax: str)-> int:
        if stt_day <= self._deli_day <= end_day:
            if uri_or_tax == 'uri':
                sum_amount += self._amount
                return sum_amount
            sum_amount += self._tax
        return sum_amount

    def _add_this1Deli_to_this25Deli(self, sum_amount: int, 
                                     stt_day: str, end_day: str,
                                     uri_or_tax)-> int:
        if stt_day <= self._deli_day <= end_day:
            if uri_or_tax == 'uri':
                sum_amount += self._amount
                return sum_amount
            sum_amount += self._tax
        return sum_amount

    def _add_this26Deli_to_thisEndDeli(self, sum_amount: int, 
                                       stt_day: str, end_day: str,
                                       uri_or_tax)-> int:
        if stt_day <= self._deli_day <= end_day:
            if uri_or_tax == 'uri':
                sum_amount += self._amount
                return sum_amount
            sum_amount += self._tax
        return sum_amount

    def _add_last26Deli_to_lastEndDeli(self, sum_amount: int, 
                                       stt_day: str, end_day: str,
                                       uri_or_tax)-> int:
        if stt_day <= self._deli_day <= end_day:
            if uri_or_tax == 'uri':
                sum_amount += self._amount
                return sum_amount
            sum_amount += self._tax
        return sum_amount
            

    def check_uris_data(self)-> None:
        
        pass

