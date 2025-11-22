'''Programação orientada a objeto - Gerenciamento de atributos'''


# códigos baseado no exemplo_1 + exemplo_3 do professor
class DescritorValidacao:
    '''Descriptor para validação automática de atributos'''

    def __init__(self, nome):
        self.nome = nome

    def __get__(self, instance, owner):
        print(f'get description: {self.nome}')
        return instance.__dict__.get(self.nome)

    def __set__(self, instance, valor):
        print(f'set description: {self.nome} = {valor}')
        if valor <= 0:
            raise ValueError(f'{self.nome} deve ser positivo')
        instance.__dict__[self.nome] = valor

    def __delete__(self, instance):
        print(f'delete: {self.nome}')
        del instance.__dict__[self.nome]


class Produto:
    # atributos de classe com descriptors
    preco = DescritorValidacao('preco')
    estoque = DescritorValidacao('estoque')

    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco  # chama __set__ automaticamente
        self.estoque = estoque  # chama __set__ automaticamente
