'''Programação orientada a objetos - Herança e polimorfismo'''

from exemplo_1 import Fila
from exemplo_2 import Bolo
from exemplo_3 import Pudim, PudimChocolate, PudimBaunilha, MeioAMeio


def exemplo_1():
    # referente a instância
    supermercado = Fila()
    loterica = Fila()
    banco = Fila()

    supermercado.s_entrar('David')
    loterica.s_entrar('Thiago')
    banco.s_entrar('Eduardo')

    print(banco.s_fila)  # ['Eduardo']
    print(loterica.s_fila)  # ['Thiago']

    supermercado.s_entrar('Marcos')
    print(supermercado.s_fila)  # ['David', 'Marcos']

    # instância s_sair()
    supermercado.s_sair()
    print(supermercado.s_fila)  # ['Marcos']

    # referente a class
    Fila.c_entrar('Mendes')
    Fila.c_entrar('Eduardo')
    Fila.c_entrar('Júlio')

    print(Fila.c_fila)  # ['Mendes', 'Eduardo', 'Júlio']

    # instância acessa a variável da class
    # ambos acessa o mesmo valor
    loterica.c_entrar('Lucas')
    print(loterica.c_fila)  # ['Mendes', 'Eduardo', 'Júlio', 'Lucas']
    banco.c_entrar('John')
    print(banco.c_fila)  # ['Mendes', 'Eduardo', 'Júlio', 'Lucas', 'John']

    # Fila.c_sair()
    Fila.c_sair()
    print(Fila.c_fila)  # ['Eduardo', 'Júlio', 'Lucas', 'John']


def exemplo_2():
    bolo_choc = Bolo('Chocolate')
    print()  # Chocolate
    print(bolo_choc.sabor)

    print(bolo_choc.pedacos)  # 12
    bolo_choc.pegar_pedaco()  # nesse momento cria-se a variavel
    print(bolo_choc.pedacos)  # 11

    print(Bolo.pedacos)  # 12
    Bolo.mudar_tamanho(16)
    print(Bolo.pedacos)  # 16

    print(bolo_choc.pedacos)  # 11 (variável da instância)

    # class
    print(
        Bolo.ingredientes()
    )  # Farinha de Trigo, Ovos, Margarina, Leite, Açucar e Chocolate
    # instância
    print(
        bolo_choc.ingredientes()
    )  # Farinha de Trigo, Ovos, Margarina, Leite, Açucar e Chocolate


def exemplo_3():
    def chocolate():
        # Pudim de Chocolate sem Polimorfismo
        chocolate = PudimChocolate('Chocolate')

        # class filha
        print()
        print(PudimChocolate.pedacos)  # 16

        # instância filha
        print()
        print(chocolate.sabor_chocolate)  # Chocolate
        print(chocolate.pedacos)  # 16

        print()
        chocolate.pegar_pedaco()
        chocolate.pegar_pedaco()
        chocolate.pegar_pedaco()
        print(chocolate.pedacos)  # 13

        print()
        print(PudimChocolate.pedacos)  # 13
        PudimChocolate.pegar_pedaco()
        print(chocolate.pedacos)  # 12
        print(PudimChocolate.pedacos)  # 12

        print()
        PudimChocolate.alterar_tamanho(20)
        print(PudimChocolate.pedacos)  # 20
        print(chocolate.pedacos)  # 20

        print()
        PudimChocolate.pegar_pedaco()
        print(chocolate.pedacos)  # 19
        print(PudimChocolate.pedacos)  # 19
        chocolate.pegar_pedaco()
        print(chocolate.pedacos)  # 18
        print(PudimChocolate.pedacos)  # 18

    def pai():
        # INSTÂNCIA DO PAI (ABSTRACTMETHOD (ABC))
        pudim_pai = Pudim('Maçã')
        print()
        print(pudim_pai.sabor)  # Maçã
        print(pudim_pai.pedacos)  # 16
        pudim_pai.pegar_pedaco()
        print(pudim_pai.pedacos)  # 15
        # TypeError: Can't instantiate abstract class Pudim without an implementation for abstract method 'ingredientes'

    def baunilha():
        # Pudim de Baunilha COM Polimorfismo
        baunilha = PudimBaunilha('Baunilha', True)

        print()
        print(PudimBaunilha.pedacos)  # 16 pega da class caso nao tenha sido alterado
        print(baunilha.sabor_baunilha)  # Baunilha
        print(baunilha.pedacos)  # 16 inicialmente da class
        print(baunilha.cobertura_extra)  # True
        baunilha.pegar_pedaco()
        baunilha.pegar_pedaco()
        print(baunilha.pedacos)  # 14 nova instancia alterada
        print(PudimBaunilha.pedacos)  # 16 permanece intacta

    def meio_a_meio():
        # Pudim de MeioAMeio COM Polimorfismo
        baunilha = PudimBaunilha()  # pega do default da classe

        # chocolate pega do defalt da classe
        meio_a_meio = MeioAMeio(pudim_baunilha=baunilha)

        print()
        # Todos estes funcionam por causa da herança:
        print(meio_a_meio.sabor_chocolate)  # Chocolate `class`->> MeioAMeio
        print(meio_a_meio.sabor_baunilha)  # Baunilha `class` ->> PudimBaunilha
        print(baunilha.cobertura_extra)  # False
        print(baunilha.ingredientes())  # TRIGO, MANTEIGA, Leite e BAUNILHA

        # Métodos também são herdados:
        print(meio_a_meio.pedacos)  # 16
        meio_a_meio.pegar_pedaco()
        PudimBaunilha.adicionar_cobertura()  # Cobertura extra adicionada!
        print(meio_a_meio.pedacos)  # 15
        print(PudimBaunilha.pedacos)  # 16

        # Segunda forma
        chocolate = PudimChocolate('Chocolate')
        baunilha = PudimBaunilha('Baunilha', True)

        meio_a_meio = MeioAMeio(chocolate, baunilha)

        print()
        # Todos estes funcionam por causa da herança:
        print(meio_a_meio.sabor_chocolate)  # Chocolate
        print(meio_a_meio.sabor_baunilha)  # Baunilha
        print(baunilha.cobertura_extra)  # True
        print(
            chocolate.ingredientes()
        )  # TRIGO, Ovos, MANTEIGA, Leite, Açucar e CHOCOLATE

        # Métodos também são herdados:
        print(meio_a_meio.pedacos)  # 16
        meio_a_meio.pegar_pedaco()
        print(meio_a_meio.pedacos)  # 15
        print(PudimBaunilha.pedacos)  # 16

        print(MeioAMeio.pedacos)  # 16
        MeioAMeio.pegar_pedaco_classe()
        MeioAMeio.pegar_pedaco_classe()
        print(MeioAMeio.pedacos)  # 14

        #  Mostra: MeioAMeio -> PudimChocolate -> PudimBaunilha -> Pudim -> object
        print(MeioAMeio.__mro__)
        # (<class 'exemplo_3.MeioAMeio'>, <class 'exemplo_3.PudimChocolate'>, <class 'exemplo_3.PudimBaunilha'>, <class 'exemplo_3.Pudim'>, <class 'object'>)

    # Testes Individuais!
    if __name__ == '__main__':
        chocolate()
        # pai()
        baunilha()
        meio_a_meio()


# Testes Individuais!
if __name__ == '__main__':
    exemplo_1()
    exemplo_2()
    exemplo_3()
