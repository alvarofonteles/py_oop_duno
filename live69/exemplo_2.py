'''Programação orientada a objeto - Interfaces e ABCs (PARTE 2)'''

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def fazer_som(self):  # direto da instância
        pass

    @classmethod
    def criar_com_nome(cls, nome):  # direto da classe
        instance = cls()
        instance.nome = nome
        return instance

    @staticmethod
    def classificar_por_idade(idade):  # direto da classe
        if idade < 1:
            return 'filhote'
        elif idade < 3:
            return 'jovem'
        else:
            return 'adulto'


class Cachorro(Animal):
    def fazer_som(self):
        return 'Au au!'


class Gato(Animal):
    def fazer_som(self):
        return 'Miau!'
