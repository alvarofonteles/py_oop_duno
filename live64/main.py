'''Programação orientada a objeto - Composição e métodos mágicos'''

from exemplo_1 import LojaCalzone, _Pedido

# loja herdada e com ABC
loja_batel = LojaCalzone('loja_3721')

# método da class abstrato
LojaCalzone.abrir_loja(loja_batel)  # Loja Batel Calzone - Curitiba Aberta!

loja_batel.numero_pedido(123)  # Ligando forno para assar: Calzone de Calabraza

print(f'Nome da Loje: {loja_batel.nome_loja}')  # Nome da Loje: Batel Calzone - Curitiba
print(f'Número do Pedido: {loja_batel.num_pedido}')  # Número do Pedido: 123
print(f'Sabor: {loja_batel.sabor}')  # Sabor: Calzone de Calabraza

loja_batel.pedido_entregue(
    123
)  # Desligando forno, gentileza retirar: Calzone de Calabraz
print(
    f'Número do Pedido Entregue: {loja_batel.num_entregue}'
)  # Número do Pedido Entregue: 123

LojaCalzone.fechar_loja(loja_batel)  # Forno Desligado!
# Loja Batel Calzone - Curitiba Fechada!
