"""
Reversed

Nao confundir com reverse() - que inverte a ordem da lista
Funçao apenas de lista.

Já Reversed funciona em qualquer iteravel
Ela Inverte o iterável.
"""

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

#Reversed com conversão

#Lista, Tupla e Conjunto(Set)
print(set(reversed(lista)))#Em conjuntos como set, a ordem não é definida

print(tuple(reversed(lista)))

print(list(reversed(lista)))

#Iterando sobre reversed
for letra in reversed('Geek University'):
    print(letra, end='')

#Iterando sobre reversed 2
print(''.join(list(reversed('Geek Universoty'))))

#Iterando sobre reversed 3 com splice
print('Geek University'[::-1])

#Reversed em  um loop for reverso
for n in reversed(range(0, 10)):
    print(n)
