from abc import ABC

class Product(ABC):
    @property
    def price():
        raise NotImplemented