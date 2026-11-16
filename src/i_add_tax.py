from abc import ABC, abstractmethod

class IAddTax(ABC):

    @abstractmethod
    def add_tax_to_dic(self)-> None:
        pass
