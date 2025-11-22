'''Programação orientada a objeto - Interfaces e ABCs (PARTE 2)'''

from exemplo_1 import MinhaImplement
from exemplo_2 import Cachorro, Gato, Animal
from exemplo_4 import Padaria, Supermercado, pessoa, Fila, Banheiro


def exemplo_1():
    '''ABC básica'''

    print('exemplo_1')
    obj = MinhaImplement()

    # [meu_metodo_abstrato] como é filha pode ser instanciada
    print(obj.meu_metodo_abstrato())  # Método exemplo `@abstractmethod` implementado!
    print(MinhaImplement.meu_metodo_de_classe())  # Método `@classmethod` implementado!
    print(MinhaImplement.meu_metodo_estático())  # Método `@staticmethod` implementado!

    print()


def exemplo_2():
    '''ABC com métodos úteis'''

    print('exemplo_2')
    billy = Cachorro.criar_com_nome('Billy')
    bebe = Gato.criar_com_nome('Bebê')

    print(f'{billy.nome}: {billy.fazer_som()}')  # Billy: Au au!
    print(f'{bebe.nome}: {bebe.fazer_som()}')  # Bebê: Miau!

    print()

    print(
        f'Classifido como: {Animal.classificar_por_idade(0.5)}'  # Direto da classe
    )  # Classifido como: filhote
    print(
        f'Classifido como: {Animal.classificar_por_idade(4)}'
    )  # Classifido como: adulto

    print()


def exemplo_3():
    '''Class Banheiro __subclasshook__'''

    print('exemplo_3')

    banheiro = Banheiro()

    print(
        f'Banheiro é subclasse de Fila? {issubclass(Banheiro, Fila)}'
    )  # Banheiro é subclasse de Fila? True

    print(
        f'Banheiro é instância de Fila? {isinstance(banheiro, Fila)}'
    )  # Banheiro é instância de Fila? True

    # Teste NEGATIVO - classe que FALTA métodos
    # class FilaIncompleta:
    #     def entrar(self, obj): # Faltam outros métodos...
    #         pass

    # print(issubclass(FilaIncompleta, Fila))  # False - subclasshook reprova!
    # AssertionError: __subclasshook__ must return either False, True, or NotImplemented

    print()


def exemplo_4():
    '''Implementações concretas da Fila'''

    print('exemplo_4')

    def padaria():

        padaria = Padaria()
        p1 = pessoa('João', 30, False, False)
        padaria.entrar(p1)

        print(
            padaria
        )  # Fila([Pessoa(nome='João', idade=30, gestante=False, deficiente=False)])
        print(f'Tamanho: {len(padaria)}')  # Tamanho: 1

    def supermercado():
        supermercado = Supermercado()

        #              [nome] [idade] [gestante] [deficiente]'
        p_gestante = pessoa('Maria', 25, True, False)  # Prioridade
        p_normal = pessoa('José', 40, False, False)  # Normal
        p_idosa = pessoa('Ana', 70, False, False)  # Prioridade
        p_deficiente = pessoa('Carlos', 30, False, True)  # Prioridade

        supermercado.entrar(p_normal)  # fila normal
        supermercado.entrar(p_gestante)  # prioridade
        supermercado.entrar(p_idosa)  # prioridade
        supermercado.entrar(p_deficiente)  # prioridade

        print()

        print(f'Fila completa: {supermercado}')
        # Fila completa:
        # Fila(
        #     [
        #         Pessoa(nome='Maria', idade=25, gestante=True, deficiente=False),
        #         Pessoa(nome='Ana', idade=70, gestante=False, deficiente=False),
        #         Pessoa(nome='Carlos', idade=30, gestante=False, deficiente=True),
        #         Pessoa(nome='José', idade=40, gestante=False, deficiente=False)
        #      ]
        # )

        print()

        print(f'soma de ambas filas: {len(supermercado)}')  # soma de ambas filas: 4
        print(
            f'procura em AMBAS filas: {p_normal in supermercado}'
        )  # procura em AMBAS filas: True

        print()

        print(f'Saindo primeiro (prioridade): {supermercado.sair()}')
        # Saindo primeiro (prioridade):
        # Pessoa(nome='Maria', idade=25, gestante=True, deficiente=False)

        print()

        print(f'Fila após saída: {supermercado}')
        # Fila após saída:
        # Fila(
        #     [
        #         Pessoa(nome='Ana', idade=70, gestante=False, deficiente=False),   # Prioridade
        #         Pessoa(nome='Carlos', idade=30, gestante=False, deficiente=True), # Prioridade
        #         Pessoa(nome='José', idade=40, gestante=False, deficiente=False)   # Normal
        #     ]
        # )

    if __name__ == '__main__':
        padaria()
        supermercado()


if __name__ == '__main__':
    exemplo_1()
    exemplo_2()
    exemplo_3()
    exemplo_4()  # testa as implementação do exemplo_3.py
