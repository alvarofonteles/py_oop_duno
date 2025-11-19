'''Programação orientada a objeto - Composição e métodos mágicos'''

from exemplo_1 import LojaCalzone
from exemplo_2 import CanarinhoPistola


def exemplo_1():
    # loja herdada e com ABC
    loja_batel = LojaCalzone('loja_3721')

    # método da class abstrato
    loja_batel.abrir_loja()  # Loja Batel Calzone - Curitiba Aberta!

    loja_batel.numero_pedido(123)  # Ligando forno para assar: Calzone de Calabraza

    print()
    print(
        f'Nome da Loje: {loja_batel.nome_loja}'
    )  # Nome da Loje: Batel Calzone - Curitiba
    print(f'Número do Pedido: {loja_batel.num_pedido}')  # Número do Pedido: 123
    print(f'Sabor: {loja_batel.sabor}')  # Sabor: Calzone de Calabraza

    print()
    loja_batel.pedido_entregue(
        123
    )  # Desligando forno, gentileza retirar: Calzone de Calabraz
    print(
        f'Número do Pedido Entregue: {loja_batel.num_entregue}'
    )  # Número do Pedido Entregue: 123

    print()
    loja_batel.fechar_loja()  # Forno Desligado!
    # Loja Batel Calzone - Curitiba Fechada!


def exemplo_2():
    def teste_canarinho_pistola():
        '''Testes completos da classe CanarinhoPistola'''

        # Criação da instância
        jogador = CanarinhoPistola('Neymar', 10)
        print()
        print(f'Nome: {jogador.nome}')  # Nome: Neymar
        print(f'Camisa: {jogador.camisa}')  # Camisa: 10
        print()

        # Teste do método __str__
        print(jogador)  # CanarinhoPistola(nome="Neymar", camisa="10")
        print()

        # Teste do método __repr__
        print(f'{repr(jogador)}')  # CanarinhoPistola(nome="Neymar", camisa="10")
        print()

        # Teste em lista (usa __repr__)
        time = [jogador, CanarinhoPistola('Gabigol', 9)]
        for jogador in time:
            print(jogador)
        print()
        # CanarinhoPistola(nome="Neymar", camisa="10")
        # CanarinhoPistola(nome="Gabigol", camisa="9")

        # Teste do MRO (Method Resolution Order)
        print(
            CanarinhoPistola.__mro__
        )  # (<class 'exemplo_2.CanarinhoPistola'>, <class 'exemplo_2.Passaro'>, <class 'exemplo_2.Jogador'>, <class 'object'>)

    if __name__ == '__main__':
        teste_canarinho_pistola()


# Testes Individuais!
if __name__ == '__main__':
    exemplo_1()
    exemplo_2()
