"""
    Modulos built-in - modulos integrados

    Que ja vem instalados no python
    Modulos built in so carregam quando utilizados.

"""

#utilizando alias, apelidos para os modulos/funçoes
import random as rdm

print(rdm.random());

#importando todas as funções utilizando *
from random import *

print(random())

#Alias para funçoes
from random import randint as rdi, random as rdm

print(rdi(5, 89))
print(rdm())

#Lidando com multiplos imports de um modulo
from random import (
    random,
    randint,
    shuffle,
    choice
)

