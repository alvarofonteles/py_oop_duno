'''Programação orientada a objeto - Sobrecarga de operadores'''


# infixo & unários
class Numero:
    def __init__(self, val):
        self.val = val

    def __add__(self, outro):  # quando objeto + algo
        # extrai o valor independente do tipo
        outro_val = outro.val if isinstance(outro, Numero) else outro
        print(f'__add__({self.val}, {outro_val})')  # mostra só valores

        return Numero(self.val + outro_val)

    def __radd__(self, outro):  # quando algo + objeto
        # extrai o valor independente do tipo
        outro_val = outro.val if isinstance(outro, Numero) else outro
        print(f'__radd__({outro_val}, {self.val})')  # mostra só valores

        return Numero(outro_val + self.val)

    def __repr__(self):
        return f'num({self.val})'
