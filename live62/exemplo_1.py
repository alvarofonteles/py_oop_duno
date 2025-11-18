'''
Programação orientada a objetos - Herança e polimorfismo
    - Atributo da `class`
    - Atributo e Método da `self` (_instância_)
    - Método da Classe `@classmethod`
'''


class Fila:
    '''
    Abstração de qualquer tipo de **Fila**
        - Supermercado
        - Processo
        - Banco
        ...
    '''

    # referente a class
    c_fila = []

    @classmethod
    def c_entrar(cls, nome):
        '''Método da Classe'''
        cls.c_fila.append(nome)

    @classmethod
    def c_sair(cls):
        cls.c_fila.pop(0)

    # referente a instância
    def __init__(self):
        self.s_fila = []

    def s_entrar(self, nome):
        '''Método da Instância'''
        self.s_fila.append(nome)

    def s_sair(self):
        self.s_fila.pop(0)
