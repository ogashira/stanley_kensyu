import csv
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
                    " RURIDT.RurNODay AS 'deli_day', RURIDT.RurUriTnk as 'tanka',"
                    " RURIDT.RurUriSu AS 'qty',"
                    " RURIDT.RurUriDay AS 'ship_day'"
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


class FetchStanKensyuData:

    def __init__(self, kensyu_data_path:str) -> None:
        self.kensyu_data_path = kensyu_data_path

    def fetch_data(self, year_month: str) -> Tuple[List[str],List[List[Any]]]:

        columns = ['No', 'unknown1', 'date', 'unknown2', 'unknown3', 
                'unknown4', 'order_no', 'unknown5', 'unknown6', 'tani', 
                'unknown7', 'unknown8', 'hin_name', 'unknown9', 'ics_no', 
                'nonyu_cd', 'tanka', 'amount', 'qty', 'deli_day', 'unknown10', 
                'unknown11', 'unknown12', 'unknown13', 'unknown14', 
                'order_day', 'unknown15', 'unknown16', 'unknown17', 
                'unknown18', 'unknown19', 'tax', 'unknown20'
        ]

        fullpath: str = rf'{self.kensyu_data_path}{year_month}.tsv'
        # year_month.tsv -> 202607.tsv

        try:
            with open(fullpath, mode="r", encoding="cp932", newline="") as f:
                reader = csv.reader(f, delimiter="\t")
                data = [[cell.strip() for cell in row]for row in reader]
                # データの空白を除いてリストに詰める
        except FileNotFoundError:
            print(f"指定されたファイルが見つかりません: {year_month}.tsv")
            raise


        return  columns, data
