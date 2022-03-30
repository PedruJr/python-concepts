"""
    Entendendo Iterator e Iterables

    Iterator ->
        - Objeto que pode ter iterado.
        - Um objeto que retorna um dado, sendo um elemento por vez, quando next() é chamado

    Iterable ->
        - Um objeto que ira retornar um iterator quando a função iter() for chamada,

    Iterables com next liberam Iterators
"""
nome = 'Geek' #Iterable
numeros = [1, 2, 3, 4, 5] #Iterable

# Retornado Iterator
it1 = iter(nome)
it2 = iter(numeros)

#Usando next() para retornar o proximo iterator
print(next(it1))
print(next(it2))