from abc import ABC
from i_add_uri import IAddUri
from i_add_tax import IAddTax
from i_data_check import IDataCheck

class IMukesakiStanUri(IAddUri, IAddTax, IDataCheck, ABC):
    pass
