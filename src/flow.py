import sys
import yaml
from typing import List, Dict, TYPE_CHECKING, Optional, Any
from date_manage import DateManage
from instance_factory import InstanceFactory
from convert_data_structure import ConvertDataStructure
from toyo_kensyu import ToyoKensyu
from get_idx import ogaColumnIndexError, GetIdx
from get_paths import get_yaml_path, get_format_excel_fullpath


# 実行時にはインポートせず、型チェックの為だけに書く
if TYPE_CHECKING:
    from i_mukesaki_toyo_uri import IMukesakiToyoUri
    from excel import Excel
class Flow:

    @classmethod
    def start(cls) ->None:

        path:str = get_yaml_path()

        # YAMLファイルを読み込む
        # {ICSNo:, stanley_factory_code:, format_fullpath:, kensyu_data_path:}
        with open(path, "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)

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

        fetch_uri_data = InstanceFactory.get_fetchUriData(
                last_month_26, this_month_end
        )
        try:
            uri_col, uri_data = fetch_uri_data.fetch_data()
        except Exception as e:
            print(f"SQLサーバーからデータ取得失敗です。中止します:{e}")
            InstanceFactory.delete_cnxn()
            sys.exit(1)

        # mukesakis_dic = {"hadano":[[uri_data_一行], [uri_data__一行]....], 
        #                  "hamamatsu": [[uri_data_一行], [uri_data__一行]..]}
        mukesakis_dic: Dict[str, List[List[Any]]]= {
                "hadano": [], "hamamatsu": [], "okazaki": [], "hiroshima": [], 
                "kumamoto":[]
        } 
        mukesaki_idx = GetIdx.get_idx(uri_col, "tokui_name")
        if mukesaki_idx == -1:
            print("必要なカラムが見つかりませんでした。tokui_name")
            sys.exit(1)
        for line in uri_data:
            if "秦野" in line[mukesaki_idx]:
                mukesakis_dic["hadano"].append(line)
                continue
            if "浜松" in line[mukesaki_idx]:
                mukesakis_dic["hamamatsu"].append(line)
                continue
            if "岡崎" in line[mukesaki_idx]:
                mukesakis_dic["okazaki"].append(line)
                continue
            if "広島" in line[mukesaki_idx]:
                mukesakis_dic["hiroshima"].append(line)
                continue
            if "熊本" in line[mukesaki_idx]:
                mukesakis_dic["kumamoto"].append(line)
                continue

        # Excelのインスタンス生成
        excel: Excel = InstanceFactory.get_Excel(get_format_excel_fullpath())
    
        # ToyoKensyuのインスタンス生成
        toyo_kensyu: ToyoKensyu = InstanceFactory.get_ToyoKensyu(mukesakis_dic, uri_col, dates_dic)

        



        
        InstanceFactory.delete_cnxn()
        print('プログラム終了です。cnxnをcloseしました')

    
