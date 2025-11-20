'''Programação orientada a objeto - Interfaces e ABCs (PARTE 1)'''

from exemplo_1 import Container as Cont, Caixa, Box, Container, Sized, Collection
from exemplo_2 import MinhaTupla
from exemplo_3 import MinhaLista


def exemplo_1():
    # container
    cont = Cont('eduardo')
    print(cont.seq)  # eduardo
    print('e' in cont)  # 'e' in Container(eduardo) | True
    print('x' in cont)  # 'x' in Container(eduardo) | False
    print(1 in cont)  # 1 in Container(eduardo) | False
    print('ardo' in cont)  # 'ardo' in Container(eduardo) | True

    # container & sized
    caixa = Caixa('dunossauro')
    print(caixa.seq)  # dunossauro
    print(len(caixa))  # 11
    print('d' in caixa)  # 'd' in Caixa(dunossauro) | True
    print('sauro' in caixa)  # 'sauro' in Caixa(dunossauro) | True
    print(issubclass(Caixa, Container))  # True
    print(issubclass(Caixa, Sized))  # True

    # collection
    box = Box('dunossauro')
    print(box.seq)  # dunossauro
    print(len(box))  # 11
    print('duno' in box)  # 'duno' in Box(dunossauro) | True

    # iteração
    for letra in box:
        print(letra, end=' ')  # d u n o s s a u r o
    print()
    print(issubclass(Box, Collection))  # True
    print(issubclass(Box, Container))  # True

    print(Collection.__mro__)  # collections.abc
    # Collection -> Sized -> Iterable -> Container -> object


def exemplo_2():
    mt = MinhaTupla(6, 4, 9, 4)

    print(mt)  # MinhaTupla(6, 4, 9, 4)

    # pega valor na posição 1
    print(mt[1])  # 4

    # usa index para encontrar posição do valor 9
    # posição onde está o 9
    print(mt.index(9))  # 2

    # se valor existe
    print(4 in mt)  # True

    # conta
    print(mt.count(4))  # 2

    # reverse
    print(list(reversed(mt)))  # [4, 9, 4, 6]


def exemplo_3():
    ml = MinhaLista(1, 2, 3)
    print(ml)  # MinhaLista(1, 2, 3)

    ml.insert(1, 99)
    print(ml)  # MinhaLista(1, 99, 2, 3)

    ml.append(100)
    print(ml)  # MinhaLista(1, 99, 2, 3, 100)

    ml[0] = 777
    print(ml)  # MinhaLista(777, 99, 2, 3, 100)

    del ml[2]
    print(ml)  # MinhaLista(777, 99, 3, 100)


# Testes Individuais!
if __name__ == '__main__':
    exemplo_1()
    exemplo_2()
    exemplo_3()
