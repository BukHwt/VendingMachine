from abc import ABC


class Coin(ABC):
    @property
    def size():
        raise NotImplemented
    
    @property
    def weight():
        raise NotImplemented