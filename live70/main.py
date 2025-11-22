'''Programação orientada a objeto - Gerenciamento de atributos'''

from exemplo_1 import Retangulo
from exemplo_2 import Produto
from exemplo_3 import NumeroPositivo
from exemplo_4 import Usuario


def exemplo_1():
    '''Properties básicas'''
    print('exemplo_1')

    ret = Retangulo(5, 3)
    # getter leitura
    print(f'área: {ret.area}')  # área: 15
    ret.largura = 7  # setter
    print(f'nova área: {ret.area}')  # nova área: 21

    ret2 = Retangulo(14, 6)
    print()
    print(f'área: {ret2.area}')  # área: 84
    ret2.largura = 9  # setter
    print(f'nova área: {ret2.area}')  # 54
    print()


def exemplo_2():
    '''Descriptors com validação'''
    print('exemplo_2')

    # acessa o decriptor na instância
    # entra no setter do description
    prod = Produto('Tablet', 800, 15)
    #   set description: preco = 800
    #   set description: estoque = 15

    # deleção em descriptor
    del prod.estoque
    # delete: estoque

    prod.estoque = 20  # entra no set do descriptor e altera
    #   set description: estoque = 20

    print()
    # entra no getter do description
    #   get description: preco
    print(f'preço: R${prod.preco} (instância)')  # preço: R$800 (instância)
    # get description: estoque
    print(f'estoque: {prod.estoque}')  # estoque: 20

    print()
    prod = Produto('Notebook', 2500, 10)
    # prod.preco = 3000  # # entra no descriptor

    print()
    print(f'preço: R${prod.preco} (instância)')  # preço: R$800 (instância)
    # prod.preco = -100  # ValueError: preco deve ser positivo
    print()

    # deleção de preço e estoque
    del prod.preco
    del prod.estoque
    print()


def exemplo_3():
    '''Property com funções'''
    print('exemplo_3')

    num = NumeroPositivo()
    num.valor = 100  # tentando setar: 100
    # acessando valor
    print(f'valor: {num.valor}')  # valor: 100

    print()
    num = NumeroPositivo()

    num.valor = 42  # tentando setar: 42
    del num.valor  # removendo valor
    num.valor = 105  # tentando setar: 105
    # acessando valor
    print(f'valor: {num.valor}')  # valor: 42
    # num.valor = -5    # ValueError: Valor deve ser positivo
    print()


def exemplo_4():
    '''Descriptors flexíveis'''
    print('exemplo_4')

    # acessa o decriptor na instância
    user = Usuario('  maria costa  ', 30)
    # set: nome =   maria costa
    # set: idade = 30

    print()
    print(f'nome: {user.nome}')  # get: nome = Maria Costa
    # nome: 👤 Maria Costa

    print(f'idade: {user.idade}')  # get: idade = 30
    # idade: 30

    print()
    # acessa o decriptor na instância
    user = Usuario('  joão silva  ', 25)
    # set: nome =   joão silva
    # set: idade = 25

    print()
    print(f'nome: {user.nome}')  # get: nome = João Silva
    # nome: 👤 João Silva

    print(f'idade: {user.idade}')  # get: idade = 25
    # idade: 25

    print()
    user.idade = -5  # set: idade = -5
    print(user.idade)  # get: idade = 0
    # 0


if __name__ == '__main__':
    exemplo_1()
    exemplo_2()
    exemplo_3()
    exemplo_4()
