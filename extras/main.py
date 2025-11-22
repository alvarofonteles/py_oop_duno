'''Programação orientada a objeto - Dataclasses (EXTRA)'''


# estudo baseado nas aulas do professor

from exemplo_1 import PessoaNamedTuple, PessoaTypedTuple, PessoaDataClass
from datetime import datetime


def exemplo_1():
    '''Comparação das 3 formas'''
    
    # 1. namedtuple (mais limitado)
    print('1. namedtuple:')
    p1 = PessoaNamedTuple('João', 25, 'Rio de Janeiro')
    print(p1)
    print(f'Nome: {p1.nome}, Idade: {p1.idade}')
    print(f'É tuple? {isinstance(p1, tuple)}')  # True
    print()
    
    # 2. NamedTuple (com tipagem)
    print('2. NamedTuple:')
    p2 = PessoaTypedTuple('Maria', 30)  # Usa cidade default
    print(p2)
    print(f'Cidade default: {p2.cidade}')
    print(f'É tuple? {isinstance(p2, tuple)}')  # True
    print()
    
    # 3. @dataclass (mais poderoso)
    print('3. @dataclass:')
    p3 = PessoaDataClass('Carlos', 35, 'Belo Horizonte')
    print(p3)
    print(f'Data criação: {p3.data_criacao}')
    print(f'Ano nascimento: {p3.ano_nascimento}')
    print(f'Cumprimento: {p3.cumprimentar()}')
    print(f'É tuple? {isinstance(p3, tuple)}')  # False
    print()


def exemplo_2():
    '''Dataclass com validações e métodos'''
    
    # Teste __post_init__ com validação
    try:
        pessoa_invalida = PessoaDataClass('Erro', -5, 'Teste')
    except ValueError as e:
        print(f'Validação funcionando: {e}')
    
    # Dataclass com data específica
    data_especifica = datetime(2023, 1, 1)
    pessoa_especial = PessoaDataClass('Ana', 28, 'Salvador', data_especifica)
    
    print()
    print(f'Pessoa com data específica:')
    print(f'Nome: {pessoa_especial.nome}')
    print(f'Data: {pessoa_especial.data_criacao}')
    print(f'Idade em 2023: {2023 - pessoa_especial.ano_nascimento}')


def exemplo_3():
    '''Comparação de igualdade'''
    
    # namedtuple
    p1 = PessoaNamedTuple('João', 25, 'SP')
    p2 = PessoaNamedTuple('João', 25, 'SP')
    print(f'namedtuple igual? {p1 == p2}')  # True
    
    # NamedTuple  
    p3 = PessoaTypedTuple('Maria', 30)
    p4 = PessoaTypedTuple('Maria', 30)
    print(f'NamedTuple igual? {p3 == p4}')  # True
    
    # @dataclass
    p5 = PessoaDataClass('Carlos', 35)
    p6 = PessoaDataClass('Carlos', 35)
    print(f'@dataclass igual? {p5 == p6}')  # True (__eq__ automático!)


if __name__ == '__main__':
    exemplo_1()
    exemplo_2() 
    exemplo_3()
    
# fonte de estudo adicional: DeepSeek