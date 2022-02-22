"""
Generators Python

Nao existe Tuple Comprehension pois eles se chaman Generators
"""

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

#List comprehension
res = [nome[0] == 'C' for nome in nomes]

#Generator, unica diferença é o conchetes
#Tem algo mais, Generator é mais performatico,
#pelos controles mais rigidos, as outras estruturas tem regras, como a key do dicionario
#os elementos que nao podem ser repetidos dos conjuntos e etc
# por ordem de menos consumo, generetor, list, set 3x mais pesado, dict x3.5 mais pesado
res = (nome[0] == 'C' for nome in nomes)

#getsizeof()
from sys import getsizeof
print(getsizeof('Geek'))