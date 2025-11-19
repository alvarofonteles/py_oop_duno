'''Programação orientada a objeto - Sobrecarga de operadores'''


class Numero:
    def __init__(self, valor):
        self.valor = valor

    # unários
    def __neg__(self):
        print(f'__neg__({self.valor})')
        return Numero(-self.valor)

    # infixo
    def __add__(self, outro):
        print(f'__add__({self.valor}, {outro.valor})')
        return Numero(self.valor + outro.valor)

    def __repr__(self):
        return f'Numero({self.valor})'


class Subtrair:
    def __sub__(self, outro):
        print(f'__sub__()')
        return Subtrair()
