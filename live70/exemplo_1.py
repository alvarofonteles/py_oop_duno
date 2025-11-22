'''Programação orientada a objeto - Gerenciamento de atributos'''


# códigos baseado no exemplo_4 + exemplo_5 do professor
class Retangulo:
    def __init__(self, largura, altura):
        self._largura = largura
        self._altura = altura

    @property
    def area(self):
        '''Calcula área automaticamente - só leitura'''
        return self._largura * self._altura

    @property
    def largura(self):
        '''Getter com validação implícita'''
        return self._largura

    @largura.setter
    def largura(self, valor):
        '''Setter com validação'''
        if valor <= 0:
            raise ValueError('Largura deve ser positiva')
        self._largura = valor
