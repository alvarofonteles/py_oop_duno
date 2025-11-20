'''Programação orientada a objeto - Interfaces e ABCs (PARTE 1)'''

# explócito issubclass
from collections.abc import Container, Sized, Collection


class Container:
    def __init__(self, seq):
        self.seq = seq

    def __contains__(self, outro):
        print(
            f"{ repr(outro) if isinstance(outro, str) else outro} in Container({self.seq})"
        )
        return outro in list(
            self.seq
        )  # converte em list pra aceitar str|int evitar # TypeError: 'in <string>'


class Caixa(Container, Sized):
    def __init__(self, seq):
        self.seq = seq

    # implícito
    def __contains__(self, outro):
        print(
            f"{ repr(outro) if isinstance(outro, str) else outro} in Container({self.seq})"
        )
        return outro in list(self.seq)

    # implícito
    def __len__(self):
        return len(self.seq)


# Collection -> Container -> Iterable -> Sized -> object
class Box(Container, Collection):  # Collection JÁ INCLUI Sized!
    def __init__(self, seq):
        self.seq = seq

    # implícito
    def __contains__(self, outro):
        print(
            f"{ repr(outro) if isinstance(outro, str) else outro} in Container({self.seq})"
        )
        return outro in list(self.seq)

    # implícito
    def __len__(self):
        return len(self.seq)

    def __iter__(self):
        return iter(self.seq)
