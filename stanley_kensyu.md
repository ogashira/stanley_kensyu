# Stanley Kensyu(スタンレー検収自動チェックプログラ厶)

```mermaid
---
title: スタンレー検収
---
classDiagram
direction TB


class IUriData{
    <<interface>>
    + add_amount():None*
    + get_uri_infos():Dict[str,Any]*
}
class ToyoUri{
    - mukesaki: str
    - order_no: str
    - tokui_name: str
    - hinban: str
    - amount: int
    - deli_day: str
    - tanka: int
    - qty: int
    - ship_day: str
    + add_amount(Dict[str,Dict[str,int]]):None
    + get_uri_infos():Dict[str,Any]
}
class StanUri{
    - mukesaki: str
    - nonyu_cd: str
    - order_no: str
    - ics_no: str
    - tokui_name: str
    - hinban: str
    - amount: int
    - tax: int
    - deli_day: str
    - tanka: int
    - qty: int
    - ship_day: str
    + add_amount(Dict[str,Dict[str,int]]):None
    + get_uri_infos():Dict[str,Any]
}
class ToyoKensyu{
    - uri_instances:Dict[str,List[IUriData]]
    - uri_amounts_dic:Dict[str,Dict[str,int]]
    - excel:Excel
    + write_amount_to_ws():None
    + get_uri_amounts_dic():Dict[str,Dict[str,int]]
}
class StanKensyu{
    - uri_instances:Dict[str,List[IUriData]]
    - uri_amounts_dic:Dict[str,Dict[str,int]]
    - excel:Excel
    + write_amount_to_ws():None
    + get_uri_amounts_dic():Dict[str,Dict[str,int]]
}
class CheckUriData{
    - toyo_kensyu:ToyoKensyu
    - stan_kensyu:StanKensyu
    - excel_ws
    + check_uri_amounts()
    + check_uris_data()
}


IUriData <|.. ToyoUri
IUriData <|.. StanUri
ToyoKensyu --> IUriData
StanKensyu --> IUriData
```

        columns = ['No', 'unknown1', 'date', 'unknown2', 'unknown3', 
                'unknown4', 'order_no', 'unknown5', 'unknown6', 'tani', 
                'unknown7', 'unknown8', 'hin_name', 'unknown9', 'ics_no', 
                'nonyu_cd', 'tanka', 'amount', 'qty', 'deli_day', 'unknown10', 
                'unknown11', 'unknown12', 'unknown13', 'unknown14', 
                'order_day', 'unknown15', 'unknown16', 'unknown17', 
                'unknown18', 'unknown19', 'tax', 'unknown20'
