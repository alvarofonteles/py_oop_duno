'''Programação orientada a objeto - Sobrecarga de operadores'''

from exemplo_1 import Dois, MinhaString, Ponto
from exemplo_2 import Numero, Subtrair
from exemplo_3 import Numero as Num
from exemplo_4 import ListaLokinha
from exemplo_5 import Contador, Vetor


# unários
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


# infixo & unários
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

    e = Subtrair() - 7  # __sub__()


# infixo & unários
def exemplo_3():
    n1 = Num(5)
    n2 = Num(10)

    print(n1 + n2)  # __add__(5, 10) | Num(15)

    n = Num(31)

    print(Num(13) + n)  # __add__(13, 31) | Num(44)
    print(n + 17)  # __add__(31, 17) | Num(48)
    print(9 + n)  # __radd__(9, 31) | Num(40)
    print(n + Num(18))  # __add__(31, 18) | Num(49)


# infixo & unários
def exemplo_4():

    ll = ListaLokinha()
    # adiciona nomamlmente com append
    ll.append(3)
    ll.append(7)
    print(ll)  # [3, 7]

    # adiciona usando o [<<] __lshift__
    ll << 9
    ll << 17
    print(ll)  # [3, 7, 9, 17]

    # remove usando o [>>] __rshift__
    print(ll)  # [3, 7, 9, 17]
    ll >> 2  # não remove na 2 (pos)
    print(ll)  # [3, 7, 17]
    ll >> -1
    print(ll)  # [3, 7]

    # invertendo usando o __neg__ com [reversed]
    ll2 = ListaLokinha()
    ll2 << 9
    ll2 << 17
    print(ll2)  # [9, 17]
    ll2.append(23)
    ll2.append(55)
    print(ll2)  # [9, 17, 23, 55]

    # lista invertida usando __neg__
    print(-ll2)  # [55, 23, 17, 9]


# IN-PLACE
def exemplo_5():

    c = Contador(5)
    c += 3  # __iadd__(5, 3)
    print(c)  # Contador(8)
    c -= 2  # __isub__(8, 2)
    print(c)  # Contador(6)


# Testes Individuais!
if __name__ == '__main__':
    exemplo_1()
    exemplo_2()
    exemplo_3()
    exemplo_4()
    exemplo_5()
