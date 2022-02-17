"""
Set comprehensions

Lembrando:
lista = [1, 2, 3]
set = {1, 2, 3, 4, 5} - nao guarda valores repetidos nem ordenação
"""

numeros = {num for num in range(1, 7)}
print(numeros)

numeros = {x: x ** 2 for x in range(10)}