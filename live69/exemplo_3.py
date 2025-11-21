'''Programação orientada a objeto - Interfaces e ABCs (PARTE 2)'''

from abc import ABC, abstractmethod
from _collections_abc import _check_methods


class Fila(ABC):
    @abstractmethod
    def __init__(self):
        self.it = []

    @abstractmethod
    def entrar(self, obj):
        pass

    @abstractmethod
    def sair(self, pos=0):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __contains__(self, obj):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @classmethod
    def __subclasshook__(cls, classe):
        if cls is Fila:
            return _check_methods(
                classe, 'entrar', 'sair', '__len__', '__contains__', '__repr__'
            )
