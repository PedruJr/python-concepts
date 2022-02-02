"""
Documentando funçoes com docstring

Docstring sao as aspas duplas triplas

no secrets, simple to use it
com declarações explicativas e diretas
so precisamos colocar o docstring dentro da função

__doc__ é uma propriedae especial que chama a documentação de uma função,


let's do a exemple:
"""

def say_hello():
    """one simple function that returns a 'hello' string"""
    return 'Hello!'

def exponencial(numero, potencia=2):
    """
    Função que retorna o exponencial de numero ou retorna o exponencial do numero pela potencia escolhida.

    :param numero: numero que desejamos apontar o exponencial
    :param potencia: potencia que queremos gerar o exponencial que por padrão é dois.
    :return: Retorna exponencial de numero por potencia
    """
    return numero ** potencia

