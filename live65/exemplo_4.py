'''Programação orientada a objeto - Sobrecarga de operadores'''


# infixo & unários
class ListaLokinha(list):
    def __add__(self, val):
        '''Soma todos os ítens da lista com val'''
        return ListaLokinha([x + val for x in self])

    def __lshift__(self, val):
        '''Fazer append na lista usando [<<]'''
        self.append(val)

    def __rshift__(self, pos):
        '''Remove um item com [>>]'''
        return self.pop(pos)

    def __neg__(self):
        '''Negando com o [reversed]'''
        return ListaLokinha(reversed(self))
