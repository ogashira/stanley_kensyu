from typing import TYPE_CHECKING, Dict, List
from i_uri_data import IUriData
from excel import Excel

class ToyoKensyu():
    def __init__(self, 
                 uri_instances: Dict[str, List[IUriData]],
                 excel: Excel) -> None:

        self._uri_instances: Dict[str,List[IUriData]] = uri_instances
        self._excel: Excel = excel


    def write_uri_mount_to_ws(self)-> None:
        uri_amounts_dic: Dict[str, Dict[str, int]] = {}
        #{'hadano':{'last26Deli_to_this25Deli': 0, 'this1Deli_to_this25Deli': 0,}    
        for mukesaki, instances in self._uri_instances.items():
            uri_amounts_dic[mukesaki] = {}

            self._add_instance_amount(mukesaki, instances, uri_amounts_dic)

        # mukesaki,period,amountをExcelに渡してｼｰﾄに書き込んでもらう
        for mukesaki, amounts_dic in uri_amounts_dic.items():
            for period, amount in amounts_dic.items():
                self._excel.write_uri_mount_to_ws_toyo(mukesaki, 
                                    period, amount)

        # amoutの合計を出してExcelに書き込む
        self._write_uri_total_to_ws(uri_amounts_dic)


    def _write_uri_total_to_ws(self, uri_amounts_dic: Dict[str, Dict[str,int]])-> None:
        # periodごとに合計を出してExcelに書き込む
        periods_total_dic: Dict[str, int] = {}
        for _, amounts_dic in uri_amounts_dic.items():
            for period, amount in amounts_dic.items():
                periods_total_dic[period] = \
                        periods_total_dic.get(period,0) + amount
        for period, amount in periods_total_dic.items():
            self._excel.write_uri_total_to_ws_toyo(period, amount)
            

    def _add_instance_amount(self, mukesaki: str, 
                             instances: List[IUriData],
                             uri_amounts_dic: Dict[str, Dict[str,int]])-> None:

        uri_amounts_dic[mukesaki]['last26Deli_to_this25Deli'] = 0
        uri_amounts_dic[mukesaki]['this1Deli_to_this25Deli'] = 0
        uri_amounts_dic[mukesaki]['this26Deli_to_thisEndDeli'] = 0
        uri_amounts_dic[mukesaki]['last26Deli_to_lastEndDeli'] = 0
        uri_amounts_dic[mukesaki]['lastShip_to_thisDeli'] = 0
        uri_amounts_dic[mukesaki]['this1Ship_to_this25Deli'] = 0

        for ins in instances:
            uri_amounts_dic[mukesaki]['last26Deli_to_this25Deli'] = (
                    ins.add_amount( mukesaki, 'last26Deli_to_this25Deli', 
                    uri_amounts_dic[mukesaki]['last26Deli_to_this25Deli'] )
                    )
            uri_amounts_dic[mukesaki]['this1Deli_to_this25Deli'] = (
                    ins.add_amount( mukesaki, 'this1Deli_to_this25Deli', 
                    uri_amounts_dic[mukesaki]['this1Deli_to_this25Deli'] )
                    )
            uri_amounts_dic[mukesaki]['this26Deli_to_thisEndDeli'] = (
                    ins.add_amount( mukesaki, 'this26Deli_to_thisEndDeli', 
                    uri_amounts_dic[mukesaki]['this26Deli_to_thisEndDeli'] )
                    )
            uri_amounts_dic[mukesaki]['last26Deli_to_lastEndDeli'] = (
                    ins.add_amount( mukesaki, 'last26Deli_to_lastEndDeli', 
                    uri_amounts_dic[mukesaki]['last26Deli_to_lastEndDeli'] )
                    )
            uri_amounts_dic[mukesaki]['lastShip_to_thisDeli'] = (
                    ins.add_amount( mukesaki, 'lastShip_to_thisDeli',
                    uri_amounts_dic[mukesaki]['lastShip_to_thisDeli'] )
                    )
            uri_amounts_dic[mukesaki]['this1Ship_to_this25Deli'] = (
                    ins.add_amount( mukesaki, 'this1Ship_to_this25Deli',
                    uri_amounts_dic[mukesaki]['this1Ship_to_this25Deli'] )
                    )

    def excel_save(self)-> None:
        self._excel.save_file()


