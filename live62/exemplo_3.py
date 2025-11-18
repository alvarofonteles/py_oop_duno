'''
Programação orientada a objetos - Herança e polimorfismo
    - Herança
    - Herança Multiplas
'''

from abc import ABC, abstractmethod


class Pudim(ABC):
    '''Classe Pai _"Abstrata"_ para ser herdada.'''

    pedacos = 16

    def __init__(self, sabor):
        self._sabor = sabor

    @property
    def sabor(self):
        return self._sabor

    @sabor.setter
    def sabor(self, valor):
        self._sabor = valor

    @classmethod
    def alterar_tamanho(cls, tamanho):
        cls.pedacos = tamanho

    # @pedacos.setter
    @classmethod
    def pegar_pedaco(cls):
        cls.pedacos -= 1

    @abstractmethod
    def ingredientes(self):
        return 'Farinha de Trigo, Ovos, Margarina, Leite, Açucar'


class PudimChocolate(Pudim):
    def __init__(self, sabor='Chocolate'):
        super().__init__(sabor)  # Chama o __init__ do pai
        self.sabor_chocolate = sabor
    
    @staticmethod
    def ingredientes():
        return 'TRIGO, Ovos, MANTEIGA, Leite, Açucar e CHOCOLATE'
    
class PudimBaunilha(Pudim):
    def __init__(
        self, sabor='Baunilha `class` ->> PudimBaunilha', cobertura_extra=False
    ):
        super().__init__(sabor)
        self.sabor_baunilha = sabor
        self.cobertura_extra = cobertura_extra

    # comportamento polimófico da instância
    def pegar_pedaco(self):
        self.pedacos -= 1

    @classmethod
    def adicionar_cobertura(cls):
        print(f'Cobertura extra adicionada!')
    @staticmethod
    def ingredientes():
        return 'TRIGO, MANTEIGA, Leite e BAUNILHA'

class MeioAMeio(PudimChocolate, PudimBaunilha):
    def __init__(self, pudim_chocolate=None, pudim_baunilha=None):
        # Extrai sabores dos objetos ou usa defaults
        sabor_chocolate = (
            pudim_chocolate.sabor_chocolate
            if pudim_chocolate
            else 'Chocolate `class` ->> MeioAMeio'
        )
        sabor_baunilha = pudim_baunilha.sabor_baunilha if pudim_baunilha else 'Baunilha'

        PudimChocolate.__init__(self, sabor_chocolate)
        PudimBaunilha.__init__(self, sabor_baunilha)
        self.sabor = "Meio a Meio"

    # comportamento polimófico da classe
    @classmethod
    def pegar_pedaco_classe(cls):
        cls.pedacos -= 1

    # comportamento polimófico da instância
    def pegar_pedaco(self):
        self.pedacos -= 1
