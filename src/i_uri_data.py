from abc import ABC, abstractmethod
from typing import Dict, List, Optional

class IUriData(ABC):

    @abstractmethod
    def add_amount(self, mukesaki: str, period: str, 
                   sum_uri: int, uri_or_tax = 'uri')-> int:
        pass
