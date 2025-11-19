'''Programação orientada a objeto - Sobrecarga de operadores'''


class Dois:
    valor = 2

    def __neg__(self):
        return f'({-self.valor}) - Negativo'

    def __pos__(self):
        return f'({+self.valor}) - Positivo'


class MinhaString:
    def __init__(self):
        self.ms = 'Deus é conosco, SEMPRE Amém!'

    def __neg__(self):
        return self.ms[::-1]


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __neg__(self):
        return Ponto(-self.x, -self.y)

    def __pos__(self):
        return Ponto(+self.x, +self.y)

    def __repr__(self):
        return f'Ponto({self.x}, {self.y})'


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
