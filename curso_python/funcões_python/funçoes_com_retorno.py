"""
Funçoes com retorno

assim como nas outras linguagens definido por um return
"""


def resultado(numero: int, multiplicador: int):
    return numero * multiplicador

#utilizando o mesmo exemplo do definindo funçoes
def diz_oi():
    return 'Oi!'

#funçoes podem ter multiplos retonos e multiplas funçoes, padrão.
#especificações apos o return nao sao executadas.

#função de jogar a moeda com random

from random import random

def joga_moeda():
    moeda = random()
    if moeda > 0.5:
        return 'Cara'
    return 'Coroa'