'''Programação orientada a objeto - Sobrecarga de operadores'''


# IN-PLACE
class Contador:
    def __init__(self, valor=0):
        self.valor = valor

    def __iadd__(self, outro):  # +=
        print(f'__iadd__({self.valor}, {outro})')
        self.valor += outro
        return self  # SEMPRE retorna self!

    def __isub__(self, outro):  # -=
        print(f'__isub__({self.valor}, {outro})')
        self.valor -= outro
        return self

    def __repr__(self):
        return f'Contador({self.valor})'


# operadores IN-PLACE essenciais
'''
Comparação
    - def __eq__(self, other):    # ==
    - def __ne__(self, other):    # !=  
    - def __lt__(self, other):    # <
    - def __le__(self, other):    # <=
    - def __gt__(self, other):    # >
    - def __ge__(self, other):    # >=
    
Aritméticos
    - def __mul__(self, other):   # *
    - def __truediv__(self, other): # /
    - def __floordiv__(self, other): # //
    - def __mod__(self, other):   # %
    - def __pow__(self, other):   # **       
'''


# EXTRA
class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vetor(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __getitem__(self, index):
        return [self.x, self.y][index]

    def __len__(self):
        return 2

    def __repr__(self):
        return f'Vetor({self.x}, {self.y})'
