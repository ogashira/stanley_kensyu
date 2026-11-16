from abc import ABC
from i_add_uri import IAddUri
from i_data_check import IDataCheck

class IMukesakiToyoUri(IAddUri, IDataCheck, ABC):
    pass
