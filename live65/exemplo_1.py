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
