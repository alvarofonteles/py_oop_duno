'''Programação orientada a objeto - Interfaces e ABCs (PARTE 1)'''

from collections.abc import MutableSequence


class MinhaLista(MutableSequence):
    def __init__(self, *valor):
        self.valor = list(valor)  # converte para lista mutável

    def __getitem__(self, idx):
        return self.valor[idx]

    def __len__(self):
        return len(self.valor)

    def __delitem__(self, idx):
        del self.valor[idx]

    def __setitem__(self, idx, valor):
        self.valor[idx] = valor

    # métodos que o professor esqueceu!
    def insert(self, idx, valor):
        self.valor.insert(idx, valor)

    def append(self, valor):
        self.valor.append(valor)  # ou self.insert(len(self), valor)

    def __repr__(self):
        return f'MinhaLista{tuple(self.valor)}'
