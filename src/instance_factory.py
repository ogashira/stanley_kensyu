from typing import Dict, TYPE_CHECKING, Any, List, Tuple, Optional
import platform
import sys
from fetch_data_for_list import IFetchDataForList, FetchStanKensyuData
from get_idx import GetIdx
from i_uri_data import IUriData
from toyo_uri import ToyoUri
from toyo_kensyu import ToyoKensyu
from stan_uri import StanUri
from stan_kensyu import StanKensyu
from excel import Excel
from get_paths import get_sql_python_module_path, get_kensyu_data_path
from fetch_data_for_list import FetchStanKensyuData

# 実行時にはインポートせず、型チェックの為だけに書く
if TYPE_CHECKING:
    from fetch_data_for_list import FetchCans


class InstanceFactory:
    '''
    各モジュールのインポートは必要な時にメソッド内で行う。
    冒頭でまとめてやると実行速度が急激に遅くなったため
    '''

    _sqlServerEffit: Any = None
    _cnxn_effit = None

    _instances: Dict[str, Any] = {}

    @classmethod
    def _setup_sql_path(cls) -> None:
        """SQLサーバー用モジュールのパスを通す (一度だけ実行)"""
        if 'sql_path_setup' in cls._instances:
            return
            
        shared_folder_path: str = r'./'
        shared_folder_path = get_sql_python_module_path()
        
        if shared_folder_path not in sys.path:
            sys.path.append(shared_folder_path)
        cls._instances['sql_path_setup'] = True


    @classmethod
    def get_sql_server_effit(cls) -> None:
        if cls._sqlServerEffit is None:
            cls._setup_sql_path()
            from sql_server_effit_addmin import SqlServer as SqlServerEffit
            cls._sqlServerEffit = SqlServerEffit()
            cls._cnxn_effit = cls._sqlServerEffit.get_cnxn()

    @classmethod
    def delete_cnxn(cls) -> None:
        if cls._sqlServerEffit:
            cls._sqlServerEffit.close()


    @classmethod
    def get_fetchUriData(cls, lastDeli:str, thisDeli:str) -> IFetchDataForList:
        from fetch_data_for_list import FetchUriData
        ins_name: str = 'fetchUriData'
        if ins_name not in cls._instances:
            cls.get_sql_server_effit()
            cls._instances[ins_name] = FetchUriData(
                    cls._cnxn_effit, lastDeli, thisDeli
                    )
        return cls._instances[ins_name]


    @classmethod
    def get_ToyoUriInstances(cls, 
            mukesakis_dic: Dict[str, List[List[Any]]],
            uri_col: List[str],
            dates_dic: Dict[str, str])-> Dict[str, List[IUriData]] :

        '''
        mukesakis_dic = {"hadano":[[uri_data_一行], [uri_data__一行]....], "hamamatsu": [[uri_data_一行], [uri_data__一行]..]}

        uri_instances(ToyoUri) = {"hadano":[ToyoUri, ToyoUri....], "hamamatsu": [ToyoUri, ToyoUri....]}
        '''
        ins_name: str = 'toyo_uri_instances'
        if ins_name in cls._instances:
            return cls._instances[ins_name]

        uri_instances: Dict[str, List[IUriData]] = {}

        for mukesaki, uris_data in mukesakis_dic.items():
            mukesakis: List[IUriData] = []
            if not uris_data:
                mukesakis.append(ToyoUri([], mukesaki, uri_col, dates_dic))
                uri_instances[mukesaki] = mukesakis
                continue

            for uri_data in uris_data:
                toyo_uri: IUriData = \
                    ToyoUri(uri_data, mukesaki, uri_col, dates_dic)
                mukesakis.append(toyo_uri)
            uri_instances[mukesaki] = mukesakis

        cls._instances[ins_name] = uri_instances

        return uri_instances


    @classmethod
    def get_ToyoKensyu(cls, 
            mukesakis_dic: Dict[str, List[List[Any]]],
            uri_col: List[str],
            dates_dic: Dict[str, str])-> ToyoKensyu:

        toyo_uri_instances: Dict[str, List[IUriData]] = \
            cls.get_ToyoUriInstances(mukesakis_dic, uri_col, dates_dic)

        excel: Excel = cls.get_Excel()

        return ToyoKensyu(toyo_uri_instances, excel)

         
    @classmethod
    def get_StanUriInstances(cls, 
            mukesakis_dic: Dict[str, List[List[Any]]],
            uri_col: List[str],
            dates_dic: Dict[str, str])-> Dict[str, List[IUriData]] :

        '''
        mukesakis_dic = {"hadano":[[uri_data_一行], [uri_data__一行]....], "hamamatsu": [[uri_data_一行], [uri_data__一行]..]}

        uri_instances(ToyoUri) = {"hadano":[ToyoUri, ToyoUri....], "hamamatsu": [ToyoUri, ToyoUri....]}
        '''
        ins_name: str = 'stan_uri_instances'
        if ins_name in cls._instances:
            return cls._instances[ins_name]

        uri_instances: Dict[str, List[IUriData]] = {}

        for mukesaki, uris_data in mukesakis_dic.items():
            mukesakis: List[IUriData] = []
            if not uris_data:
                mukesakis.append(StanUri([], mukesaki, uri_col, dates_dic))
                uri_instances[mukesaki] = mukesakis
                continue

            for uri_data in uris_data:
                stan_uri: IUriData = \
                    StanUri(uri_data, mukesaki, uri_col, dates_dic)
                mukesakis.append(stan_uri)
            uri_instances[mukesaki] = mukesakis

        cls._instances[ins_name] = uri_instances

        return uri_instances


    @classmethod
    def get_StanKensyu(cls, 
            mukesakis_dic: Dict[str, List[List[Any]]],
            uri_col: List[str],
            dates_dic: Dict[str, str])-> StanKensyu:

        stan_uri_instances: Dict[str, List[IUriData]] = \
            cls.get_StanUriInstances(mukesakis_dic, uri_col, dates_dic)

        excel: Excel = cls.get_Excel()

        return StanKensyu(stan_uri_instances, excel)

         
    @classmethod
    def get_Excel(cls)-> Excel:

        ins_name: str = 'get_Excel'
        if ins_name not in cls._instances:
            cls._instances[ins_name] = Excel()
        return cls._instances[ins_name]


    @classmethod
    def get_FetchStanKensyuData(cls)-> FetchStanKensyuData:
        kensyu_data_path: str = get_kensyu_data_path()
        return FetchStanKensyuData(kensyu_data_path)
