"""
O modulo random

O modulo no python é qualquer arquivo que podemos importar para
utilizar suas funçoes.

Um grupo de modulos forma um pacote.

Random é um modulo nativo.
"""

#podemos importar o modulo ou func especificas dentro do modulo
#Não é recomendado importar todo o modulo, o ideial é importar os metodos desejados.
#No caso se você sabe a função desejada voce pode importala diretamente

#podemos segurar ctrl e acessar o modulo random e verificar seus atributos e funcs
import random #import completo

#Chamamos a função pelo nome do pacote utilizando um . para chamar o metodo.
print(random.random())#Numero aleatorio entre 0 e 1

##Import de func especifica " FROM modulo IMPORT func"
from random import random, randint, choice, shuffle

for i in range(6):
    print(randint(1, 61), end= ', ') # começa em 1 e vai até 60

#Metodo choice(lista) ele seleciona um item da lista aleatoriamente
#So passar o iteravel
print(choice('geek university'))

##Função shuffle que embaralha, podemos destacar uma carta atravez do .pop que destaca a ultima
print(shuffle('cartas'))







