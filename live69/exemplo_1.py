'''Programação orientada a objeto - Interfaces e ABCs (PARTE 2)'''

from abc import ABC, abstractmethod


class MinhaABC(ABC):
    @abstractmethod
    def meu_metodo_abstrato(self):  # contrato obrigatório
        pass

    @classmethod
    def meu_metodo_de_classe(cls):  # herdável
        pass

    @staticmethod
    def meu_metodo_estático():  # herdável
        pass


class MinhaImplement(MinhaABC):
    def meu_metodo_abstrato(self):  # obrigatório (sem decorator)
        return 'Método exemplo `@abstractmethod` implementado!'

    @classmethod
    def meu_metodo_de_classe(cls):  # opcional mas com decorator se sobrescrever
        return 'Método `@classmethod` implementado!'

    @staticmethod
    def meu_metodo_estático():  # opcional mas com decorator se sobrescrever
        return 'Método `@staticmethod` implementado!'
