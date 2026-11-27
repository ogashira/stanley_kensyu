import sys
from typing import List, Dict, TYPE_CHECKING, Optional, Any, Tuple
from get_idx import GetIdx

class DataProcessing:

    def create_mukesakis_data(self, col: List[str], 
                           data: List[List[Any]]) -> Dict[str, List[List[Any]]]:
        '''
        toyo_col: ['uri_no', 'order_no', 'tokui_name', 'hinban', 'amount', 
              'deli_day', 'tanka', 'ship_day']
        stan_col = ['No', 'unknown1', 'date', 'unknown2', 'unknown3', 
                'unknown4', 'order_no', 'unknown5', 'unknown6', 'tani', 
                'unknown7', 'unknown8', 'hin_name', 'unknown9', 'ics_no', 
                'nonyu_cd', 'tanka', 'amount', 'qty', 'deli_day', 'unknown10', 
                'unknown11', 'unknown12', 'unknown13', 'unknown14', 
                'order_day', 'unknown15', 'unknown16', 'unknown17', 
                'unknown18', 'unknown19', 'tax', 'unknown20'
         mukesakis_data = {"hadano":[[uri_data_一行], [uri_data__一行]....], 
                          "hamamatsu": [[uri_data_一行], [uri_data__一行]..]}
        '''
        mukesakis_data: Dict[str, List[List[Any]]]= {
                "hadano": [], "hamamatsu": [], "okazaki": [], "hiroshima": [], 
                "kumamoto":[]
        } 
        mukesaki_idx = GetIdx.get_idx(col, "tokui_name")
        if mukesaki_idx == -1:
            print("必要なカラムが見つかりませんでした。tokui_name")
            sys.exit(1)

        for line in data:
            if "秦野" in line[mukesaki_idx]:
                mukesakis_data["hadano"].append(line)
                continue
            if "浜松" in line[mukesaki_idx]:
                mukesakis_data["hamamatsu"].append(line)
                continue
            if "岡崎" in line[mukesaki_idx]:
                mukesakis_data["okazaki"].append(line)
                continue
            if "広島" in line[mukesaki_idx]:
                mukesakis_data["hiroshima"].append(line)
                continue
            if "熊本" in line[mukesaki_idx]:
                mukesakis_data["kumamoto"].append(line)
                continue

        return mukesakis_data


    def edit_stan_data(self, col: List[str], 
                       data: List[List[Any]],
                       ics_nos: Dict[str, str], 
                       factory_codes: Dict[str, str],
                       dates_dic: Dict[str, str]) -> Tuple[List[str],List[List[Any]]]:
        '''
        stan_col = ['No', 'unknown1', 'date', 'unknown2', 'unknown3', 
                'unknown4', 'order_no', 'unknown5', 'unknown6', 'tani', 
                'unknown7', 'unknown8', 'hin_name', 'unknown9', 'ics_no', 
                'nonyu_cd', 'tanka', 'amount', 'qty', 'deli_day', 'unknown10', 
                'unknown11', 'unknown12', 'unknown13', 'unknown14', 
                'order_day', 'unknown15', 'unknown16', 'unknown17', 
                'unknown18', 'unknown19', 'tax', 'unknown20'
        '''

        deli_day_idx = GetIdx.get_idx(col, "deli_day")
        for line in data:
            line[deli_day_idx] = "20" + line[deli_day_idx]  # 20260726のようにする

        last26: str = dates_dic['last_month'] + '26'
        thisEnd: str = dates_dic['this_month_end']

        # indexの取得
        order_no_idx = GetIdx.get_idx(col, "order_no")
        nonyu_cd_idx = GetIdx.get_idx(col, "nonyu_cd")
        ics_no_idx = GetIdx.get_idx(col, "ics_no")
        amount_idx = GetIdx.get_idx(col, "amount")
        deli_day_idx = GetIdx.get_idx(col, "deli_day")
        tanka_idx = GetIdx.get_idx(col, "tanka")
        qty_idx = GetIdx.get_idx(col, "qty")
        tax_idx = GetIdx.get_idx(col, "tax")

        edited_data: List[List[Any]] = []
        for line in data:
            inner: List[Any] = []
            if line[deli_day_idx] >= last26 and line[deli_day_idx] <= thisEnd:
                inner.append(line[order_no_idx])
                tokui_name = factory_codes[line[nonyu_cd_idx]]
                inner.append(tokui_name)
                hinban = ics_nos[line[ics_no_idx]]
                inner.append(hinban)
                inner.append(line[amount_idx])
                inner.append(line[deli_day_idx])
                inner.append(line[tanka_idx])
                inner.append(line[qty_idx])
                inner.append(line[tax_idx])
                edited_data.append(inner)

        col = ['order_no', 'tokui_name', 'hinban', 'amount',
                'deli_day', 'tanka', 'qty', 'tax']

        return col, edited_data
