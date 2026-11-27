import sys
import yaml
from typing import List, Dict, TYPE_CHECKING, Optional, Any
from date_manage import DateManage
from data_processing import DataProcessing
from instance_factory import InstanceFactory
from toyo_kensyu import ToyoKensyu
from stan_kensyu import StanKensyu
from get_paths import get_yaml_path, get_format_excel_fullpath


# 実行時にはインポートせず、型チェックの為だけに書く
if TYPE_CHECKING:
    from i_uri_data import IUriData
    from excel import Excel
class Flow:

    @classmethod
    def start(cls) ->None:

        date_manage = DateManage()
        this_month = date_manage.year_month_input() 

        this_month_end: str= date_manage.get_this_month_end(this_month)
        last_month: str = date_manage.get_last_month(this_month)
        last_month_end: str = date_manage.get_last_month_end(this_month)
        last_month_26 = last_month + '26'

        dates_dic: Dict[str, str] = {
                'this_month': this_month, 
                'last_month': last_month, 
                'this_month_end': this_month_end, 
                'last_month_end': last_month_end
        }

        '''
        toyoデータ>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        '''
        fetch_uri_data = InstanceFactory.get_fetchUriData(
                last_month_26, this_month_end
        )
        try:
            toyo_data_col, toyo_data = fetch_uri_data.fetch_data()
        except Exception as e:
            print(f"SQLサーバーからデータ取得失敗です。中止します:{e}")
            InstanceFactory.delete_cnxn()
            sys.exit(1)

        # mukesakis_data = {"hadano":[[data_一行], [data__一行]....], 
        #                  "hamamatsu": [[data_一行], [data__一行]..]}
        data_processing = DataProcessing()
        mukesakis_data_toyo = data_processing.create_mukesakis_data(
                                               toyo_data_col, toyo_data)
    
        # ToyoKensyuのインスタンス生成
        toyo_kensyu: ToyoKensyu = InstanceFactory.get_ToyoKensyu(
                mukesakis_data_toyo, toyo_data_col, dates_dic
        )
        # toyo_kensyuのデータをExcelに書き込む
        toyo_kensyu.write_amount_to_ws()
        toyo_kensyu.excel_save()

        '''
        stanleyデータ>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        '''
        # StanleyKensyu_dataを取得する。
        fetch_stan_kensyu_data = InstanceFactory.get_FetchStanKensyuData()
        try:
            stan_data_col, stan_data_last_month = \
                              fetch_stan_kensyu_data.fetch_data(last_month) 
            _, stan_data_this_month = fetch_stan_kensyu_data.fetch_data(this_month)
        except FileNotFoundError as e:
            print(f"スタンレー検収データがみつかりません。中止します:{e}")
            sys.exit(1)

        # 先月と今月のデータを結合する
        stan_data = stan_data_last_month + stan_data_this_month

        # stanley_kensyu.yamlを取得
        yaml_path: str = get_yaml_path()
        with open(yaml_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        ics_nos: Dict[str, str] = data["ICSNo"]
        factory_codes: Dict[str, str] = data["stanley_factory_code"]
        if not(ics_nos and factory_codes):
            print("stanley_kensyu.yamlのICSNoまたはstanley_factory_codeがありません。中止します")
            sys.exit(1)

        # stan_data_colとstan_dataを編集する
        edited_col, edited_stan_data = data_processing.edit_stan_data(
                stan_data_col, stan_data, ics_nos, factory_codes, dates_dic)
        # mukesakis_data_stan = {"hadano":[[data_一行], [data__一行]....], 
        #                  "hamamatsu": [[data_一行], [data__一行]..]}
        mukesakis_data_stan = data_processing.create_mukesakis_data(
                                               edited_col, edited_stan_data)
        # StanKensyuのインスタンス生成
        stan_kensyu: StanKensyu = InstanceFactory.get_StanKensyu(
                mukesakis_data_stan, edited_col, dates_dic
        )
        # stan_kensyuのデータをExcelに書き込む
        stan_kensyu.write_amount_to_ws()
        stan_kensyu.excel_save()

        








        
        InstanceFactory.delete_cnxn()
        print('プログラム終了です。cnxnをcloseしました')

    
