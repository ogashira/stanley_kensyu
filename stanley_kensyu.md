# Stanley Kensyu(スタンレー検収自動チェックプログラ厶)

```mermaid
---
title: スタンレー検収
---
classDiagram
direction TB


class UriData{
    <<interface>>
    + add_amount():None*
}
class ToyoUri{
    - mukesaki: str
    - order_no: str
    - tokui_name: str
    - hinban: str
    - amount: int
    - deli_day: str
    - tanka: int
    - ship_day: str
    + add_amount(Dict[str,Dict[str,int]]):None
    + check_uris_data():None
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
    - ship_day: str
    + add_amount(Dict[str,Dict[str,int]]):None
    + check_uris_data(MukesakiToyoUri):None
}
class ToyoKensyu{
    - uri_instances:Dict[str,List[IMukesakiToyoUri]]
    - excel:Excel
    + write_uri_mount_to_ws():None
}
class StanKensyu{
    - uri_instances:Dict[str,List[IMukesakiStanUri]]
    - excel:Excel
    + write_uri_mount_to_ws():None
    + write_tax_mount_to_ws():None
}
class CheckUriData{
    - mukesakis_toyo_uri:Dict[str,IMukesakiToyoUri]
    - mukesakis_stan_uri:Dict[str,IMukesakiStanUri]
    - excel_ws
    + check_uris_data()
}


UriData <|.. ToyoUri
UriData <|.. StanUri
ToyoKensyu --> UriData
StanKensyu --> UriData
```

        columns = ['No', 'unknown1', 'date', 'unknown2', 'unknown3', 
                'unknown4', 'order_no', 'unknown5', 'unknown6', 'tani', 
                'unknown7', 'unknown8', 'hin_name', 'unknown9', 'ics_no', 
                'nonyu_cd', 'tanka', 'amount', 'qty', 'deli_day', 'unknown10', 
                'unknown11', 'unknown12', 'unknown13', 'unknown14', 
                'order_day', 'unknown15', 'unknown16', 'unknown17', 
                'unknown18', 'unknown19', 'tax', 'unknown20'
