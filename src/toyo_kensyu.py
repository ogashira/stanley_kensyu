from typing import TYPE_CHECKING, Dict, List
from i_mukesaki_toyo_uri import IMukesakiToyoUri

class ToyoKensyu():
    def __init__(self, uri_instances: Dict[str, List[IMukesakiToyoUri]]) -> None:
        self._uri_instances: Dict[str,List[IMukesakiToyoUri]] = uri_instances

