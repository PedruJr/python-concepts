"""
Entendendo Comprehensions (Compreensão de listas) - pt 1

Geramos novas listas a partir de dados processados vindos de outro interavel
#Sua sintaxe, por ser lista é limitada por []
[dado for dado in iterável]
"""

numeros = [1, 2, 3, 4, 5]

#isto é list comprehensions
res = [numero * 10 for numero in numeros]

"""
-Entendendo a compreensão, divido em duas partes
- a primeira for numero in numeros
- a segunda é fazer numero * dez
"""

#Agora utilizando loop

numeros_dobrados = []
for numero in numeros:
    numeros_dobrados = numero * 2
    numeros_dobrados.append(numeros_dobrados)

#list compreehension, podemos mandar uma expressao antes do for
print([numero * 2 for numero in [1, 2, 3, 4, 5]])

#Outros exemplos

nome = 'Jack Johnsons'
print([letra.upper() for letra in nome])

amigos = ['maria', 'julia', 'joao', 'guilherme', 'vanessa']
print([amigo.upper for amigo in amigos])

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

print([str(numero) for numero in [1, 2,]])


"""
List comprehension - pt. 2

Podemos adicionar estruturas condicionais logicas aos list comprehensions
"""
#Exemplos

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

#Refatorado

pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2 != 0]

#Exemplo 2

result = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]