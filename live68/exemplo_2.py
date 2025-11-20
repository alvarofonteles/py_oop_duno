'''Programação orientada a objeto - Interfaces e ABCs (PARTE 1)'''

from collections.abc import Sequence


class MinhaTupla(Sequence):
    def __init__(self, *valor):  # args
        self.valor = valor

    # pega o indice/posição
    def __getitem__(self, idx):
        return self.valor[idx]

    # conta cada iteração
    def __len__(self):
        return len(self.valor)
    
    def __repr__(self):
        return f'MinhaTupla{tuple(self.valor)}'
