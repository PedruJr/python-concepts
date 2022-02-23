"""
Min e max

max() - Maior numero de uma lista/iteravel/dois ou mais elementos

min() - Menor numero de uma lista/iteravel/dois ou mais elementos
"""

lista = [1, 8, 15, 99, 34, 129]
print(max(lista))#129 maior numero
#Podemos utilizar em qualquer iteravel

print(min(lista))#1 menor numero
#Podemos utilizar em qualquer iteravel

dicionario = {'a': 1, 'b': 5, 'c': 4, 'd': 34}
print(max(dicionario.values()))

print(min(lista))#1 menor numero
#Podemos utilizar em qualquer iteravel

#max compara dois valores entre si enviando dois parametros
#Ex: print(max(val1, val2, val3))

#Possivel utilizar em caracteres tambem
print(max('a', 'ab', 'abc'))#Neste caso quanto mais letras maior e tambem por ordem do alfabeto mesmo com mais letras
print(max('a', 'b', 'c', 'f'))#neste caso F é maior, depende da posiçao do alfabeto

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

#Exemplos diferentes
print(max(nomes, key=lambda nome: len(nome)))

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 3},
    {"titulo": "Rock'n'roll", "tocou": 32},
]

print(max(musicas, key=lambda musica: musica['tocou']))



