'''
Programação orientada a objetos - Herança e polimorfismo
    - Atributo da `class`
    - Atributo e Método da `self` (_instância_)
    - Método da Classe `@classmethod`
    - Método sem **_"sem dono"_** `@staticmethod`
'''


class Bolo:
    '''Bolo com 12 pedaços'''

    pedacos = 12

    def __init__(self, sabor):
        self.sabor = sabor

    def pegar_pedaco(self):
        '''
        Variável `self.pedacos` criada no `__init__`
            - Tem **mesmo** nome
            - Procura na instância `self` primeiro
            - Não **encontrando**, procura na `class`
            - Após chamada, passa de fato a **existir** (_independente_)
        '''

        self.pedacos -= 1

    @classmethod
    def mudar_tamanho(cls, tam):
        '''Altera o valor da variável/atributo da `class`'''
        cls.pedacos = tam

    @staticmethod
    def ingredientes():
        '''
        Método `@staticmethod` sem referência de `class` ou `self` (instância)
            - Sem "dono"
            - Acessada por ambos
        '''
        return 'Farinha de Trigo, Ovos, Margarina, Leite, Açucar e Chocolate'
