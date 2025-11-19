'''Programação orientada a objeto - Composição e métodos mágicos'''

class Passaro:
    def __init__(self, nome):
        self.nome = nome

class Jogador:
    def __init__(self, camisa):
        self.camisa = camisa

class CanarinhoPistola(Passaro, Jogador):
    def __init__(self, nome, camisa):
        Passaro.__init__(self, nome)
        Jogador.__init__(self, camisa)

    def __str__(self):
        return f'CanarinhoPistola(nome="{self.nome}", camisa="{self.camisa}")'

    def __repr__(self):
        return f'CanarinhoPistola(nome="{self.nome}", camisa="{self.camisa}")'