'''Programação orientada a objeto - Interfaces e ABCs (PARTE 2)'''

from collections import namedtuple
from exemplo_3 import Fila

pessoa = namedtuple('Pessoa', 'nome idade gestante deficiente')


class Padaria(Fila):
    def __init__(self):
        self.it = []

    def entrar(self, obj):
        self.it.append(obj)

    def sair(self, pos=0):
        return self.it.pop(pos)

    def __len__(self):
        return len(self.it)

    def __contains__(self, obj):
        return obj in self.it

    def __repr__(self):
        return f'Fila({self.it})'


class Supermercado(Fila):
    def __init__(self):
        self.fila_normal = []
        self.fila_prioridade = []

    def entrar(self, obj):
        if isinstance(obj, pessoa):
            if obj.idade > 64 or obj.gestante or obj.deficiente:
                self.fila_prioridade.append(obj)
            else:
                self.fila_normal.append(obj)
        else:
            raise NotImplementedError

    def sair(self, pos=0):
        if self.fila_prioridade:
            return self.fila_prioridade.pop(pos)
        return self.fila_normal.pop(pos)

    def __len__(self):
        return len(self.fila_normal) + len(self.fila_prioridade)

    def __contains__(self, obj):
        return obj in self.fila_normal or obj in self.fila_prioridade

    def __repr__(self):
        return f'Fila({self.fila_prioridade + self.fila_normal})'


# __subclasshook__ para banheiro
class Banheiro:

    def __init__(self):
        self.it = []

    def entrar(self, obj):
        pass

    def sair(self, pos=0):
        pass

    def __len__(self):
        pass

    def __contains__(self, obj):
        pass

    def __repr__(self):
        pass
