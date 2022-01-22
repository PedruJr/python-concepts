"""
Modulo Collections - Counter (Contador)

Collection - High-performance Container Datetypes

Containers com dados de alta performance

Counter -> Recebe um interavel como parametro e cria um tipo de COLLECTION COUNTER que é parecido
com um dicionario, porem recebe como chave o nome do elemento e o seu valor vira a quantidade de ocorrencias deste elemento

"""

#Utilizando o Counter, é necessario importar

from collections import Counter

lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 45, 50, 55]

#Utilizando o Counter
resultado = Counter(list)

#o resultado fica separado por uma : seu primeiro valor é qual elemento o segundo e quantas
#vezes ex a cima ({ 1:5, 3:5, 2:4})
print(resultado)

##Podemos usar o counter em qualquer interavel como uma string, assim para cada letra ou valor ele replica a chave
# como exemplo Counter('Geek University') = ({'e':3, 'i':2 }

#podemos combinar funcionalidades como mandar um array de palavras e fazer o count countar elas,
#assim ele nao contara letra por letra.

#Podemos utilisar Counter(resultado) resultado.most_common(5))