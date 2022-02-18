"""
Map

Com map, fazemos mapeamento de valores para função

"""
import math

def area(r):
    """Calcula a area de um circulo com raio 'r'. """
    return math.py * (r ** 2)

raios = [2, 5, 7.1, 0.3, 10, 44]

#Forma comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

#Forma 2 com map, recebe dois parametros a função e uma lista iteravel
# o seu retorno é um map object
areas = map(area, raios)
print(list(areas))

#Forma 3 map com lambda
print(list(map(lambda r: math.pi * (r **2), raios)))

#apos a primeira utilização ele zera o resultado, interessante pois limpa a memoria
#o objeto gerado é Map Object: Funçao(parametro1), Funcao(parametro2) ....
cidades = [('Berlim', 29),('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Nova York', 28),
 ('Londre', 22)]

## aqui ele recebe somente um dado mas utilizando map podemos fazer a utilização com varios parametros vindos do interavel
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))