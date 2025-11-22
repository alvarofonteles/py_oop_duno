'''Programação orientada a objeto - Gerenciamento de atributos'''


# códigos correto e funcional do exemplo_7 do professor
class DescritorFlexivel:
    '''Descriptor que aceita personalizar'''

    def __init__(self, nome, validacao=None, transformacao=None):
        self.nome = f'_{nome}'  # nome interno
        self.validacao = validacao
        self.transformacao = transformacao

    def __get__(self, instance, owner):
        if instance is None:
            return self
        valor = getattr(instance, self.nome)
        print(f'get: {self.nome[1:]} = {valor}')

        # aplica transformação no get, se existir
        if self.transformacao:
            return self.transformacao(valor)
        return valor

    def __set__(self, instance, valor):
        print(f'set: {self.nome[1:]} = {valor}')

        # aplica validação, se existir
        if self.validacao:
            valor = self.validacao(valor)

        setattr(instance, self.nome, valor)

    def __delete__(self, instance):
        print(f'delete: {self.nome[1:]}')
        delattr(instance, self.nome)


class Usuario:
    # descriptors com comportamentos customizados
    # limpa e capitaliza
    # adiciona emoji no get
    nome = DescritorFlexivel(
        'nome', validacao=lambda x: x.strip().title(), transformacao=lambda x: f'👤 {x}'
    )

    # garante idade ≥ 0
    idade = DescritorFlexivel('idade', validacao=lambda x: max(0, int(x)))

    def __init__(self, nome, idade):
        self.nome = nome  # chama descriptor
        self.idade = idade  # chama descriptor
