"""
Zip - Cria um interavel (Zip object) agrega eleementos dos iteraveis passados como entrada nos parametros

"""

# Exemplo
lista1 = [1, 2, 3]
lista2 = [4, 5 ,6]

#cria uma nova tupla unindo o conteudo das mesmas posições nas listas zipadas
#lista1[0], lista2[0]
zip1 = zip(lista1, lista2)

#Caso voce passe uma lista maior que as outras, o zip para o processo na menor lista iteravel
#Podemos utilizar diferentes tipos de dados para fazer os novos conjutnos, inclusive strings
#Podemos passar listas de tuplas

#utilizando descompactaçao
dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))

##Exemplos complexos
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Pedro', 'Carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}


#utilizando map
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))