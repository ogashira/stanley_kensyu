from i_uri_data import IUriData
from typing import Dict, List, Any
from get_idx import GetIdx

class ToyoUri(IUriData):
    '''
    uri_col =  ['uri_no', 'order_no', 'tokui_name'," 'hinban', 'amount', 
                'deli_day', 'tanka', 'ship_day']
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
        self._ship_day: str = ''

        uri_no_idx: int = GetIdx.get_idx(uri_col, 'uri_no')
        order_no_idx: int = GetIdx.get_idx(uri_col, 'order_no')
        tokui_name_idx: int = GetIdx.get_idx(uri_col, 'tokui_name')
        hinban_idx: int = GetIdx.get_idx(uri_col, 'hinban')
        amount_idx: int = GetIdx.get_idx(uri_col, 'amount')
        deli_day_idx: int = GetIdx.get_idx(uri_col, 'deli_day')
        tanka_idx: int = GetIdx.get_idx(uri_col, 'tanka')
        ship_day_idx: int = GetIdx.get_idx(uri_col, 'ship_day')

        if uri_data:
            self._uri_no: str = uri_data[uri_no_idx]
            self._order_no: str = uri_data[order_no_idx]
            self._tokui_name: str = uri_data[tokui_name_idx]
            self._hinban: str = uri_data[hinban_idx]
            self._amount: int = uri_data[amount_idx]
            self._deli_day: str = uri_data[deli_day_idx]
            self._tanka: int = uri_data[tanka_idx]
            self._ship_day: str = uri_data[ship_day_idx]


    def add_amount(self, mukesaki: str, period: str, 
                   sum_uri: int, uri_or_tax = 'uri')-> int:

        if self._mukesaki != mukesaki:
            return sum_uri + 0

        last1: str = self._dates_dic['last_month'] + '01'
        last26: str = self._dates_dic['last_month'] + '26'
        lastEnd: str = self._dates_dic['last_month_end']
        this1: str = self._dates_dic['this_month'] + '01'
        this25: str = self._dates_dic['this_month'] + '25'
        this26: str = self._dates_dic['this_month'] + '26'
        thisEnd: str = self._dates_dic['this_month_end']

        if period == 'last26Deli_to_this25Deli':
            sum_uri = self._add_last26Deli_to_this25Deli(
                    sum_uri, last26, this25
            )
        if period == 'this1Deli_to_this25Deli':
            sum_uri = self._add_this1Deli_to_this25Deli(
                    sum_uri, this1, this25
            )
        if period == 'this26Deli_to_thisEndDeli':
            sum_uri = self._add_this26Deli_to_thisEndDeli(
                    sum_uri, this26, thisEnd
            )
        if period == 'last26Deli_to_lastEndDeli':
            sum_uri = self._add_last26Deli_to_lastEndDeli(
                    sum_uri, last26, lastEnd
            )
        if period == 'lastShip_to_thisDeli':
            sum_uri = self._add_lastShip_to_thisDeli(
                    sum_uri, last1, lastEnd, this1, this25
            )
        if period == 'this1Ship_to_this25Deli':
            sum_uri = self._add_this1Ship_to_this25Deli(
                    sum_uri, this1, this25, this1, this25
            )

        return sum_uri

    def _add_last26Deli_to_this25Deli( self, sum_uri: int, 
                                       stt_day: str, end_day: str)-> int:
        if stt_day <= self._deli_day <= end_day:
            sum_uri += self._amount
        return sum_uri

    def _add_this1Deli_to_this25Deli(self, sum_uri: int, 
                                      stt_day: str, end_day: str)-> int:
        if stt_day <= self._deli_day <= end_day:
            sum_uri += self._amount
        return sum_uri

    def _add_this26Deli_to_thisEndDeli(self, sum_uri: int, 
                                        stt_day: str, end_day: str)-> int:
        if stt_day <= self._deli_day <= end_day:
            sum_uri += self._amount
        return sum_uri

    def _add_last26Deli_to_lastEndDeli(self, sum_uri: int, 
                                        stt_day: str, end_day: str)-> int:
        if stt_day <= self._deli_day <= end_day:
            sum_uri += self._amount
        return sum_uri
            
    def _add_lastShip_to_thisDeli(self, sum_uri: int, 
                                   ship_stt_day: str, ship_end_day: str,
                                   deli_stt_day: str, deli_end_day: str)-> int:
        if (ship_stt_day <= self._ship_day <= ship_end_day and 
            deli_stt_day <= self._deli_day <= deli_end_day):
            sum_uri += self._amount
        return sum_uri

    def _add_this1Ship_to_this25Deli(self, sum_uri: int, 
                                   ship_stt_day: str, ship_end_day: str,
                                   deli_stt_day: str, deli_end_day: str)-> int:
        if (ship_stt_day <= self._ship_day <= ship_end_day and 
            deli_stt_day <= self._deli_day <= deli_end_day):
            sum_uri += self._amount
        return sum_uri


    def check_uris_data(self)-> None:
        
        pass

