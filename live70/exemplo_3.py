'''Programação orientada a objeto - Gerenciamento de atributos'''


# códigos baseado no exemplo_6 do professor
class NumeroPositivo:
    def __init__(self):
        self._valor = None

    def get_valor(self):
        '''Getter tradicional'''
        print('acessando valor')
        return self._valor

    def set_valor(self, novo_valor):
        '''Setter com validação'''
        print(f'tentando setar: {novo_valor}')
        if novo_valor is not None and novo_valor <= 0:
            raise ValueError('Valor deve ser positivo')
        self._valor = novo_valor

    def del_valor(self):
        '''Deleter'''
        print('removendo valor')
        del self._valor

    # property() com funções explicitas
    valor = property(get_valor, set_valor, del_valor, 'Número positivo validado')
