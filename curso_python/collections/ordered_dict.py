"""
Collections - Ordered Dict

Temos este dicionario por que a ordem de inserção nao é garantida
Resolvemos o problema com Ordered Dict
"""

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

#Fazendo o import
from collections import OrderedDict

dicionario2 =  OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

#utilizando o OrderedDict
for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

#Ao realizar um compare entre dicionarios, a ordem dos fatores nao altera os produtos
#Resultando em true
#Porem com OrderedDict precisa ser com ordens iguais para resultar em true

