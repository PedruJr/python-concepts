"""
Tuples - Tuplas

    -> São parecidas com listas. diferenças
    -> Tuplas sao representads por () parenteses, diferente da lista [].
    -> Tuplas sao imutaveis, ao se criar uma tupla, ela nao muda.
    -> Toda operação em uma tupla gera uma nova tuplas.
    -> Tuplas sao mais rapidas que listas.
    -> dados imutaveis trazem maior segurança.
"""
#Exemplos.
tupla1 = (1, 2, 3, 4, 5)
print(tupla1)

#Ambas sao tuplas.
tupla2 = 1, 2, 3, 4 ,5

#Nao é uma tupla.
tupla3 = (3)

#È uma tupla.
tupla4 = (3,)

#Gerando tupla dinamica pelo tuple().
tupla5 = tuple(range(5))

#Desempacotamento de tupla.
tupla6 = ('Farao', 'tribal', 'mt loko') #tupla

#Desempacotamento por definir em variaveis em ordem, separadas por , sendo igual a tupla definida.
rei, tribo, doido = tupla6

#Podemos concatenar tuplas em uma nova tupla
tupla3 = tupla1 + tupla2

#ela é mutavel com outra tupla
tupla1 = tupla1+tupla2

##verificar se esta na tupla
print ('farao' in tupla3)#retorna true

##iterando uma tupla como uma lista, for, while, enumerate.

##podemos contar a tupla com count.

##usamos para listas que não seram modificadas, como as de meses.

#acessos a tupla funcionam como uma lista
print(tupla1[1])

#relembrar é viver, slicing
print(tupla1[1:4:print("sick sick")])





