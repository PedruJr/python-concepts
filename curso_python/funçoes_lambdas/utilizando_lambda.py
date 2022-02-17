"""
Utilizando lambdas - ou Funçoes Anonimas/Sem nome

Como criar e como aplicar, como map, filter, reduce, len, zip

# Função em python

def soma(a, b):
    return a + b

# Função expressa em lambda

lambda x: 3 * x
"""

def funcao(x):
    return x * 3

## Expressão lambda

lambda x: 3 * x

#Como utilizar o lambda?
calc = lambda x: 3 * x

print(calc(4))

#Lambdas de multiplos parametros/entradas separados com virgula
#strip() remove espaços no final e começo
#title() capitaliza uma string, letra inicial maiscula e outras minusculas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' angela', 'jolly'))
print(nome_completo(' angela      ', 'jolley'))

#lambda sem entrada, com retorno
python_lover = lambda: 'Como não amar Python?'

#Another example
autores = ['Rick Martin', 'Jorge Willys', 'Antony Ropquins', 'Oslo Biboco Diagonal', 'Mat C. Damon', 'Nicholas Sparks']

##normalmente usado
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())


#Função Quadrática
# f(x) = a * x ** 2 + b * x + c

#Definindo a funçao