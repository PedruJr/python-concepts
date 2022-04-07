"""
    Decorators com diferentes assinaturas

    A assinatura de uma função é representada pelo seu retorno,
    nome e parametros de entrada
"""

#Relembrando
def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o {nome}'

#Perceber quantos parametros são necessarios ao declarar o decorator
#Com mais de um parametro
#Porem podemos resolver utilizando o DECORATOR PATTERN *args ou *kwargs
@gritar
def ordenar(principal, acompanhamento):
    return f'Ola, gostaria de {principal}, acompnhado de' \
           f'{acompanhamento}, por favor'

##Refatoração com decorator pattern

def gritar2(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar2
def saudacao2(nome):
    return f'Olá, eu sou o {nome}'

#Perceber quantos parametros são necessarios ao declarar o decorator
#Com mais de um parametro
#Porem podemos resolver utilizando o DECORATOR PATTERN *args ou *kwargs
@gritar2
def ordenar2(principal, acompanhamento):
    return f'Ola, gostaria de {principal}, acompnhado de' \
           f'{acompanhamento}, por favor'

print(saudacao2('Felicity'))

print(ordenar2('Picanha', 'batata frita'))

#OBS: VALE A PENA LEMPRAR QUE PODEMOS NOMEAR OS PARAMETROS
print(ordenar2(acompanhamento='Picanha', principal='batata frita'))

#Decorator com argumento
#Verifica o primeiro argumento

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor Incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra()
    return interna()

@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

print(soma_dez(10,12))