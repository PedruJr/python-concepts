"""
Sobre Tuples

São parecidas com listas, diferenças

Tuplas sao representads por () parenteses, diferente da lista []
Tuplas sao definidas por ,

Tuplas sao imutaveis, ao se criar uma tupla, ela nao muda,
toda operação em uma tupla gera uma nova tuplas


tuplas sao mais rapidas que listas
dados imutaveis trazem maior segurança
"""
#Exemplos
tupla1 = (1, 2, 3, 4, 5)
print(tupla1)

#ambas sao tuplas
tupla2 = 1, 2, 3, 4 ,5

#nao é uma tupla
tupla3 = (3)

#é uma tupla
tupla4 = (3,)

#gerando tupla dinamica pelo tuple()
tupla5 = tuple(range(5))

#desempacotamento de tupla
tupla6 = ('Farao', 'tribal', 'mt loko')

rei, tribo, doido = tupla6

#podemos concatenar tuplas em uma nova tupla
tupla3 = tupla1 + tupla2

#ela é mutavel com outra tupla
tupla1 = tupla1+tupla2

##verificar se esta na tupla
print ('farao' in tupla3)

##iterando uma tupla como uma lista, for, while, enumerate

##podemos contar a tupla com count

##usamos para listas que não seram modificadas, como as de meses.

#acessos a tupla funcionam como uma lista
print(tupla1[1])

#relembrar é viver, slicing
print(tupla1[1:4:print("sick sick")])





