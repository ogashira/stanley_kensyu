from typing import Dict, TYPE_CHECKING, Any, List, Tuple, Optional
import platform
import sys
from fetch_data_for_list import IFetchDataForList
from get_idx import GetIdx
from i_mukesaki_toyo_uri import IMukesakiToyoUri
from mukesaki_toyo_uri import MukesakiToyoUri

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
        if platform.system() == 'Linux':
            shared_folder_path = \
                r'/mnt/public/技術課ﾌｫﾙﾀﾞ/200. effit_data/ﾏｽﾀ/sql_python_module'
        elif platform.system() == 'Windows':
            shared_folder_path = \
                r'//192.168.1.247/共有/技術課ﾌｫﾙﾀﾞ/200. effit_data/ﾏｽﾀ/sql_python_module'
        
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
    def get_HadanoToyoUri(cls, 
            uris_data: List[List[Any]], mukesaki)-> List[IMukesakiToyoUri]:
        
        uri_instances: List[IMukesakiToyoUri] = []

        if not uris_data:
            uri_instances.append(MukesakiToyoUri([], mukesaki))
            return uri_instances

        for uri_data in uris_data:
            toyo_uri: IMukesakiToyoUri = \
                MukesakiToyoUri(uri_data, mukesaki)
            uri_instances.append(toyo_uri)
        return uri_instances

