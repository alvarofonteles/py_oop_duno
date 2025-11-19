'''Programação orientada a objeto - Sobrecarga de operadores'''

from exemplo_1 import Dois, MinhaString, Ponto
from exemplo_2 import Numero, Subtrair


def exemplo_1():
    dois = Dois()
    print(repr(-dois))  # (-2) - Negativo
    print(+dois)  # (2) - Positivo

    ms = MinhaString()
    print(-ms)  # !mémA ERPMES ,ocsonoc é sueD

    ponto = Ponto(1, 3)
    print(-ponto)  # Ponto(-1, -3)
    print(repr(-ponto))  # Ponto(-1, -3)
    print(str(+ponto))  # Ponto(1, 3)


def exemplo_2():
    a = Numero(5)
    b = Numero(16)
    c = Numero(17)
    d = Numero(21)

    # utiliza o code srt e repr
    print(-a)  # __neg__(5) | Numero(-5)
    print(a + b)  #  __add__(5, 16) | Numero(21)
    print(str(-c))  # __neg__(17) | Numero(-17)
    print(repr(c + d))  #  __add__(17, 21) | Numero(38)

    e = Subtrair() - 7 # __sub__()


# Testes Individuais!
if __name__ == '__main__':
    exemplo_1()
    exemplo_2()
