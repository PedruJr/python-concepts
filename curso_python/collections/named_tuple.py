"""
Modulo Collections - Named Tuple

#recap tupla
tupla = (1, 2, 3)

#Named tupla
#Tuplas diferenciadas onde especificamos nome e parametros
"""
#Import
from collections import namedtuple

#Precisar definir nome e parametro.

#Forma1 - Declaração named tuple
#                    declaração, variaveis da declaraçao
cahorro = namedtuple('cachorro', 'idade raca nome')

#forma2 - Declaração com virgula e declaração dos atributos entre conchetes
cachorros = namedtuple('cachorro', 'idade, raca, nome')
cachorreds = namedtuple('cachorro', ['idade', 'raca', 'nome'])

ray = cachorreds(idade=2, raca='Chow-chow', nome= 'Ray')
# Parece uma interface esse named tuple, acessamos os atributos
# como um array [0] = primeiro atributo
#ex1:
print(ray[0])
#ex2: podemos apontar o nome do atributo que fica bem melhor
print(ray.idade)