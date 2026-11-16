from i_mukesaki_toyo_uri import IMukesakiToyoUri
from typing import Dict, List, Any

class MukesakiToyoUri(IMukesakiToyoUri):
    def __init__(self, uris_data: List[Any], mukesaki: str) -> None:
        self._mukesaki= mukesaki # hadanoなど 
        self._last26Deli_to_this25Deli: int = 0
        self._this1Deli_to_this25Deli: int = 0
        self._this26Deli_to_thisEndDeli: int = 0
        self._last26Deli_to_lastEndDeli: int = 0
        self._lastShip_to_thisDeli: int = 0
        self._this1Ship_to_this25Deli: int = 0

        if uris_data:
            self._last26Deli_to_this25Deli = self._ 

            self._this1Deli_to_this25Deli: int = 0
            self._this26Deli_to_thisEndDeli: int = 0
            self._last26Deli_to_lastEndDeli: int = 0
            self._lastShip_to_thisDeli: int = 0
            self._this1Ship_to_this25Deli: int = 0


    def add_uri_to_dic(self, uris: Dict[str,Dict[str,int]])-> None: 
        pass

    def check_uris_data(self)-> None:
        
        pass

