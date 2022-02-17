"""
Dictionary Comprehension

Criando um dicionario
dicionario = {'a': 1, 'b': 2, 'c': 4}

Diferente de conjunto que nao tem chave, apenas valor.
conjunto/set = {1, 2 ,3}

#Sintaxe
{chave:valor}
{chave:valor for valor in iterável}

"""
#Exemplos
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

#Criando um dict especificando chave e valor
quadrado = {valor: valor ** 2 for valor in numeros}

#misturar chaves com valores
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range (0, len(chaves))}
print(mistura)

#Exemplo com logica condicional
numeros = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}

print(res)