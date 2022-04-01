"""
    Funções de maior grandeza - Higher Order Functions - HOF

    Passar funções como argumentos
    Quando uma linguagem de programação permite que usamos este conceito
    podemos ter funções que retornam funções ou passar funçoes como argumetos.
    Usar variaveis como funçoes.

    Funções são First Class Citizen - Cidadoes de primeira clase HOF



"""

#Exemplos - Definindo funções
def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

#Funções aninhadas, nested functions, função dentro de funçao
#Inner Functions
#Ex:

def dividir(a, b):
    return a / b

def calcular(num1, num2 , funcao):
    return funcao(num1, num2)

#Testando. passando uma funçao para a funçao como parametro
print(calcular(4, 3, somar))

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai', 'Suma Daqui', 'Gosto de voce'))
    return humor() + pessoa

#Retornando funções de outras funções
def faz_me_rir():
    def rir():
        return choice(('hahahaaha', 'kkkkkkk', 'hsdauhsusa'))
    return rir #sem conchetes nao executa, podemos registrar em uma var

rindo = faz_me_rir()
print(rindo)#executa o rir

##Nested functions atendem o corpo do metodo

