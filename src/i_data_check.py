from abc import ABC, abstractmethod

class IDataCheck(ABC):

    @abstractmethod
    def check_uris_data(self)-> None:
        pass
