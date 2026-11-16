import csv
import yaml
import platform
import warnings
from typing import List, Any, Tuple, Dict
from abc import ABC, abstractmethod

warnings.filterwarnings('ignore', category=UserWarning)

class IFetchDataForList(ABC):

    @abstractmethod
    def fetch_data(self)-> Tuple[List[str],List[List[Any]]]:
        pass


class FetchUriData(IFetchDataForList):

    def __init__(self, cnxn, lastDeli:str, thisDeli:str ) -> None:
        self.cnxn = cnxn
        self.lastDeli = lastDeli # last26Deli 先月26日
        self.thisDeli = thisDeli # thisEndDeli 今月末日


    def fetch_data(self) -> Tuple[List[str],List[List[Any]]]:

        cursor = self.cnxn.cursor()

        sqlQuery = ("SELECT RURIDT.RurUNo AS 'uri_no'," 
                    " RURIDT.RurCMNo AS 'order_no'," 
                    " RURIHD.RurTokNam1 AS 'tokui_name',"
                    " RURIDT.RurHinCD AS 'hinban', RURIDT.RurUriKin AS 'amount'," 
                    " RURIDT.RurNODay as 'deli_day', RURIDT.RurUriTnk as 'tanka',"
                    " RURIDT.RurUriDay as 'ship_day'"
                    " From dbo.RURIDT"
                    " LEFT JOIN dbo.RURIHD"
                    " ON RURIDT.RurUNo = RURIHD.RurUNo"
                    " WHERE RURIHD.RurTokNam1 LIKE '%スタンレー電気株式会社%'"
                    " AND RURIDT.RurNODay >=" + self.lastDeli + 
                    " AND RURIDT.RurNODay <=" + self.thisDeli +
                    " ORDER BY RURIDT.RurUriDay"
                    )


        data_list: List[List[Any]] = []
        cursor.execute(sqlQuery)

        # 1. カラム名を取得（リスト内包表記）
        # cursor.description は (名前, 型, 表示サイズ, ...) というタプルのリスト
        columns = [column[0] for column in cursor.description]

        # 4. 2次元リストへ変換
        # fetchall() はタプルのリストを返すため、リスト内包表記で各行をリスト化します
        try:
            data_list = [list(row) for row in cursor.fetchall()]
        except Exception as e:
            print(f'データベースfetch中に予期せぬエラーです fetch_uri_data')
            raise Exception from e
        finally:
            cursor.close()
            # cnxnは呼び出しもとでクローズ

        return columns, data_list

        

class FetchCans:

    def fetch_data(self) -> Dict[str, Any]:

        path: str = r'\\192.168.1.247\共有\技術課ﾌｫﾙﾀﾞ\26. 製品DB\新ﾌｫｰﾏｯﾄ\営業部master\output_notification.yml'
        if platform.system() == 'Linux':
            path = r'/mnt/public/技術課ﾌｫﾙﾀﾞ/26. 製品DB/新ﾌｫｰﾏｯﾄ/営業部master/output_notification.yml'

        # YAMLファイルを開いて読み込む
        with open(path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        return data
