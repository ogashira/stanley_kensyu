from abc import ABC, abstractmethod
from typing import Dict, List, Optional

class IAddUri(ABC):

    @abstractmethod
    def add_uri_to_dic(self, uris: Dict[str,Dict[str,int]])-> None:
        pass
