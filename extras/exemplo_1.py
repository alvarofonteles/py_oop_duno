'''Programação orientada a objeto - Dataclasses (EXTRA)'''

# esrudo baseado nas aulas do professor

from collections import namedtuple
from typing import NamedTuple
from dataclasses import dataclass
from datetime import datetime


# 1. FORMA ANTIGA - collections.namedtuple
PessoaNamedTuple = namedtuple('PessoaNamedTuple', ['nome', 'idade', 'cidade'])


# 2. FORMA INTERMEDIÁRIA - typing.NamedTuple  
class PessoaTypedTuple(NamedTuple):
    nome: str
    idade: int
    cidade: str = 'São Paulo'  # Valor default


# 3. FORMA MODERNA - @dataclass
@dataclass
class PessoaDataClass:
    nome: str
    idade: int
    cidade: str = 'São Paulo'
    data_criacao: datetime = None
    
    def __post_init__(self):
        '''Executado automaticamente após __init__'''
        if self.idade < 0:
            raise ValueError('Idade não pode ser negativa')
        
        if self.data_criacao is None:
            self.data_criacao = datetime.now()
    
    @property
    def ano_nascimento(self):
        '''Property calculada - só dataclass permite fácil integração'''
        ano_atual = datetime.now().year
        return ano_atual - self.idade
    
    def cumprimentar(self):
        '''Método customizado'''
        return f'Olá, eu sou {self.nome} de {self.cidade}!'
        
# fonte de estudo adicional: DeepSeek