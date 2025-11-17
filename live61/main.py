'''
Programação orientada a objetos - Introdução
'''

from exemplo_1 import Fila


def exemplo_1():
    supermercado = Fila()
    loterica = Fila()
    banco = Fila()

    supermercado.entrar('David')
    loterica.entrar('Thiago')
    banco.entrar('Eduardo')

    print(banco.fila)  # ['Eduardo']
    print(loterica.fila)  # ['Thiago']

    supermercado.entrar('Marcos')
    print(supermercado.fila)  # ['David', 'Marcos']


# Testes Individuais!
if __name__ == '__main__':
    exemplo_1()
