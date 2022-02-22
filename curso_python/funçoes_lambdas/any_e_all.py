"""
Any e All

all() - Retorna true mesmo se todos os elementos do iteravel sao verdadeiros ou ainda se o iteravel esta vazio.

"""

#Exemplo de all
print(all([0, 1, 2, 3, 4]))#Todos os numeros sao verdadeiros? false, um valor é zero

print(all([0, 1, 2, 3, 4]))#True

print(all([]))#True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Caligolas', 'Calica']

print(all([nome[0] == 'C' for nome in nomes]))

print(all([letra for letra in 'eiof' if letra in 'aeiou']))

