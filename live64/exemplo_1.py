'''Programação orientada a objeto - Composição e métodos mágicos'''

from abc import ABC, abstractmethod


class Calzone(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def abrir_loja(self):
        pass


class LojaCalzone(Calzone):
    _loja = {'loja_3721': 'Batel Calzone - Curitiba'}

    def __init__(self, nome_loja):
        self.nome_loja = self._loja[nome_loja]
        super().__init__(self.nome_loja)

    def abrir_loja(self):
        print(f'Loja {self.nome} Aberta!')

    def numero_pedido(self, num_pedido=0):
        self.num_pedido = num_pedido

        if self.num_pedido <= 0:
            raise ValueError('Erro: Falta o número do pedido')

        self._pedito = _Pedido(self.num_pedido)
        self.sabor = self._pedito.sabor
        # ligando o forno
        self._ligar_forno()

    def _ligar_forno(self):
        self._forno = _Forno(self.sabor)
        self._forno._ligar()

    def pedido_entregue(self, num_entregue):
        self.num_entregue = num_entregue
        self._desligar_forno(True)

    def _desligar_forno(self, entregue):
        self._forno = _Forno(self.sabor)
        self._forno._desligar(entregue)

    def fechar_loja(self):
        self._desligar_forno(False)
        print(f'Loja {self.nome_loja} Fechada!')


class _Forno:
    def __init__(self, nome):
        self._nome = nome

    def _ligar(self):
        print(f'Ligando forno para assar: {self._nome}')

    def _desligar(self, entregue):
        if entregue:
            print(f'Desligando forno, gentileza retirar: {self._nome}')
        else:
            print('Forno Desligado!')


class _Pedido:
    _sabor = {
        123: 'Calzone de Calabraza',
        321: 'Calzone de Mussarela',
        456: 'Calzone de Peperone',
        654: 'Calzone Quatro Queijo',
    }

    def __init__(self, num_pedido=123):
        self.pedido = num_pedido

    @property
    def sabor(self):
        return self._sabor[self.pedido]
