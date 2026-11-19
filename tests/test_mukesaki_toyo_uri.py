import pytest
from typing import List, Dict, Any
from src.mukesaki_toyo_uri import MukesakiToyoUri
from src.instance_factory import InstanceFactory
from src.get_idx import GetIdx

@pytest.fixture
def get_uri_data():
    fetch_uri_data = InstanceFactory.get_fetchUriData('20260726', '20260831')
    col, data = fetch_uri_data.fetch_data()
    mukesakis_dic: Dict[str, List[List[Any]]]= {
            "hadano": [], "hamamatsu": [], "okazaki": [], "hiroshima": [], 
            "kumamoto":[]
    } 
    mukesaki_idx = GetIdx.get_idx(col, "tokui_name")
    for line in data:
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
    return col, mukesakis_dic

    
@pytest.fixture
def get_ToyoUriInstances(get_uri_data):
    col, mukesakis_dic = get_uri_data
    dates_dic: Dict[str, str] = {
            'this_month': '202608', 
            'last_month': '202607', 
            'this_month_end': '20260831', 
            'last_month_end': '20260731'
    }

    uri_instances = InstanceFactory.get_ToyoUriInstances(mukesakis_dic, col, dates_dic)
    return uri_instances

def test_add_uri_to_dic(get_ToyoUriInstances):
    uri_instances = get_ToyoUriInstances
    hadano_last26Deli_to_this25Deli = 0
    hadano_this1Deli_to_this25Deli = 0
    hadano_this26Deli_to_thisEndDeli = 0
    hadano_last26Deli_to_lastEndDeli = 0
    hadano_lastShip_to_thisDeli = 0
    hadano_this1Ship_to_this25Deli = 0
    hamamatsu_last26Deli_to_this25Deli = 0
    hamamatsu_this1Deli_to_this25Deli = 0
    hamamatsu_this26Deli_to_thisEndDeli = 0
    hamamatsu_last26Deli_to_lastEndDeli = 0
    hamamatsu_lastShip_to_thisDeli = 0
    hamamatsu_this1Ship_to_this25Deli = 0
    okazaki_last26Deli_to_this25Deli = 0
    okazaki_this1Deli_to_this25Deli = 0
    okazaki_this26Deli_to_thisEndDeli = 0
    okazaki_last26Deli_to_lastEndDeli = 0
    okazaki_lastShip_to_thisDeli = 0
    okazaki_this1Ship_to_this25Deli = 0
    hiroshima_last26Deli_to_this25Deli = 0
    hiroshima_this1Deli_to_this25Deli = 0
    hiroshima_this26Deli_to_thisEndDeli = 0
    hiroshima_last26Deli_to_lastEndDeli = 0
    hiroshima_lastShip_to_thisDeli = 0
    hiroshima_this1Ship_to_this25Deli = 0
    kumamoto_last26Deli_to_this25Deli = 0
    kumamoto_this1Deli_to_this25Deli = 0
    kumamoto_this26Deli_to_thisEndDeli = 0
    kumamoto_last26Deli_to_lastEndDeli = 0
    kumamoto_lastShip_to_thisDeli = 0
    kumamoto_this1Ship_to_this25Deli = 0
    for mukesaki, uris in uri_instances.items():
        for uri in uris:
            hadano_last26Deli_to_this25Deli = uri.add_uri_to_dic(
                    'hadano', 'last26Deli_to_this25Deli', 
                    hadano_last26Deli_to_this25Deli)
            hadano_this1Deli_to_this25Deli = uri.add_uri_to_dic(
                    'hadano', 'this1Deli_to_this25Deli', 
                    hadano_this1Deli_to_this25Deli)
            hadano_this26Deli_to_thisEndDeli = uri.add_uri_to_dic(
                    'hadano', 'this26Deli_to_thisEndDeli', 
                    hadano_this26Deli_to_thisEndDeli)
            hadano_last26Deli_to_lastEndDeli = uri.add_uri_to_dic(
                    'hadano', 'last26Deli_to_lastEndDeli', 
                    hadano_last26Deli_to_lastEndDeli)
            hadano_lastShip_to_thisDeli = uri.add_uri_to_dic(
                    'hadano', 'lastShip_to_thisDeli', 
                    hadano_lastShip_to_thisDeli)
            hadano_this1Ship_to_this25Deli = uri.add_uri_to_dic(
                    'hadano', 'this1Ship_to_this25Deli', 
                    hadano_this1Ship_to_this25Deli)
            hamamatsu_last26Deli_to_this25Deli = uri.add_uri_to_dic(
                    'hamamatsu', 'last26Deli_to_this25Deli', 
                    hamamatsu_last26Deli_to_this25Deli)
            hamamatsu_this1Deli_to_this25Deli = uri.add_uri_to_dic(
                    'hamamatsu', 'this1Deli_to_this25Deli', 
                    hamamatsu_this1Deli_to_this25Deli)
            hamamatsu_this26Deli_to_thisEndDeli = uri.add_uri_to_dic(
                    'hamamatsu', 'this26Deli_to_thisEndDeli', 
                    hamamatsu_this26Deli_to_thisEndDeli)
            hamamatsu_last26Deli_to_lastEndDeli = uri.add_uri_to_dic(
                    'hamamatsu', 'last26Deli_to_lastEndDeli', 
                    hamamatsu_last26Deli_to_lastEndDeli)
            hamamatsu_lastShip_to_thisDeli = uri.add_uri_to_dic(
                    'hamamatsu', 'lastShip_to_thisDeli', 
                    hamamatsu_lastShip_to_thisDeli)
            hamamatsu_this1Ship_to_this25Deli = uri.add_uri_to_dic(
                    'hamamatsu', 'this1Ship_to_this25Deli', 
                    hamamatsu_this1Ship_to_this25Deli)
            okazaki_last26Deli_to_this25Deli = uri.add_uri_to_dic(
                    'okazaki', 'last26Deli_to_this25Deli', 
                    okazaki_last26Deli_to_this25Deli)
            okazaki_this1Deli_to_this25Deli = uri.add_uri_to_dic(
                    'okazaki', 'this1Deli_to_this25Deli', 
                    okazaki_this1Deli_to_this25Deli)
            okazaki_this26Deli_to_thisEndDeli = uri.add_uri_to_dic(
                    'okazaki', 'this26Deli_to_thisEndDeli', 
                    okazaki_this26Deli_to_thisEndDeli)
            okazaki_last26Deli_to_lastEndDeli = uri.add_uri_to_dic(
                    'okazaki', 'last26Deli_to_lastEndDeli', 
                    okazaki_last26Deli_to_lastEndDeli)
            okazaki_lastShip_to_thisDeli = uri.add_uri_to_dic(
                    'okazaki', 'lastShip_to_thisDeli', 
                    okazaki_lastShip_to_thisDeli)
            okazaki_this1Ship_to_this25Deli = uri.add_uri_to_dic(
                    'okazaki', 'this1Ship_to_this25Deli', 
                    okazaki_this1Ship_to_this25Deli)
            hiroshima_last26Deli_to_this25Deli = uri.add_uri_to_dic(
                    'hiroshima', 'last26Deli_to_this25Deli', 
                    hiroshima_last26Deli_to_this25Deli)
            hiroshima_this1Deli_to_this25Deli = uri.add_uri_to_dic(
                    'hiroshima', 'this1Deli_to_this25Deli', 
                    hiroshima_this1Deli_to_this25Deli)
            hiroshima_this26Deli_to_thisEndDeli = uri.add_uri_to_dic(
                    'hiroshima', 'this26Deli_to_thisEndDeli', 
                    hiroshima_this26Deli_to_thisEndDeli)
            hiroshima_last26Deli_to_lastEndDeli = uri.add_uri_to_dic(
                    'hiroshima', 'last26Deli_to_lastEndDeli', 
                    hiroshima_last26Deli_to_lastEndDeli)
            hiroshima_lastShip_to_thisDeli = uri.add_uri_to_dic(
                    'hiroshima', 'lastShip_to_thisDeli', 
                    hiroshima_lastShip_to_thisDeli)
            hiroshima_this1Ship_to_this25Deli = uri.add_uri_to_dic(
                    'hiroshima', 'this1Ship_to_this25Deli', 
                    hiroshima_this1Ship_to_this25Deli)
            kumamoto_last26Deli_to_this25Deli = uri.add_uri_to_dic(
                    'kumamoto', 'last26Deli_to_this25Deli', 
                    kumamoto_last26Deli_to_this25Deli)
            kumamoto_this1Deli_to_this25Deli = uri.add_uri_to_dic(
                    'kumamoto', 'this1Deli_to_this25Deli', 
                    kumamoto_this1Deli_to_this25Deli)
            kumamoto_this26Deli_to_thisEndDeli = uri.add_uri_to_dic(
                    'kumamoto', 'this26Deli_to_thisEndDeli', 
                    kumamoto_this26Deli_to_thisEndDeli)
            kumamoto_last26Deli_to_lastEndDeli = uri.add_uri_to_dic(
                    'kumamoto', 'last26Deli_to_lastEndDeli', 
                    kumamoto_last26Deli_to_lastEndDeli)
            kumamoto_lastShip_to_thisDeli = uri.add_uri_to_dic(
                    'kumamoto', 'lastShip_to_thisDeli', 
                    kumamoto_lastShip_to_thisDeli)
            kumamoto_this1Ship_to_this25Deli = uri.add_uri_to_dic(
                    'kumamoto', 'this1Ship_to_this25Deli', 
                    kumamoto_this1Ship_to_this25Deli)
    assert hadano_last26Deli_to_this25Deli == 154385
    assert hadano_this1Deli_to_this25Deli == 154385
    assert hadano_this26Deli_to_thisEndDeli == 0
    assert hadano_last26Deli_to_lastEndDeli == 0
    assert hadano_lastShip_to_thisDeli == 0
    assert hadano_this1Ship_to_this25Deli == 154385
    assert hamamatsu_last26Deli_to_this25Deli == 824300
    assert hamamatsu_this1Deli_to_this25Deli == 613700
    assert hamamatsu_this26Deli_to_thisEndDeli == 70200
    assert hamamatsu_last26Deli_to_lastEndDeli == 210600
    assert hamamatsu_lastShip_to_thisDeli == 140400
    assert hamamatsu_this1Ship_to_this25Deli == 473300
    assert okazaki_last26Deli_to_this25Deli == 158745
    assert okazaki_this1Deli_to_this25Deli == 130860
    assert okazaki_this26Deli_to_thisEndDeli == 0
    assert okazaki_last26Deli_to_lastEndDeli == 27885
    assert okazaki_lastShip_to_thisDeli == 37545
    assert okazaki_this1Ship_to_this25Deli == 93315
    assert hiroshima_last26Deli_to_this25Deli == 0
    assert hiroshima_this1Deli_to_this25Deli == 0
    assert hiroshima_this26Deli_to_thisEndDeli == 0
    assert hiroshima_last26Deli_to_lastEndDeli == 0
    assert hiroshima_lastShip_to_thisDeli == 0
    assert hiroshima_this1Ship_to_this25Deli == 0
    assert kumamoto_last26Deli_to_this25Deli == 0
    assert kumamoto_this1Deli_to_this25Deli == 0
    assert kumamoto_this26Deli_to_thisEndDeli == 0
    assert kumamoto_last26Deli_to_lastEndDeli == 0
    assert kumamoto_lastShip_to_thisDeli == 0
    assert kumamoto_this1Ship_to_this25Deli == 0


