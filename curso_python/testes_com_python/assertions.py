"""
    Assertions - Afirmações
    -> Palavra reservada em python 'assert' realizar arfirmações
     nos testes, checando se é valido ou não. Caso a expressão
     seja verdadeira o retorno sera 'None', do contrario, levanta
     um erro do tipo 'AssertionError'.
    -> Podemos especificar um segundo argumento opcional, ou ate
    personalizar a mensagem de erro.
    -> Podemos utilizar assert em qualquer lugar do python.
    -> Caso o python seja executado com -O, todas as validações são
    descartadas.

"""

def soma_numeros_positivos(a, b):
    #Garantir uma entrega de parametros conforme o desejado na
    #confirmação.
    assert a > 0 and b > 0, 'Numeros não sao Positivos'
    return a+b

def comer_fast_food(comida):
    #verificar se o parametro esta em uma lista
    assert comida in [
        'pizza',
        'sorvete',
        'doce',
        'batata frita',
        'cachorro quente',
    ], 'A comida não é fastfood'
    return f'Estou comendo {comida}'

