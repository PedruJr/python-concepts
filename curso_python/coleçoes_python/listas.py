"""
    Definindo listas

    -> Listas em python funcionam como vetores e matrizes, arrays no caso,
sao DINAMICO e guardam QUALQUER tipo de dado.
    -> Tipagem de forma dinamica, diferente das linguagens fortemente tipadas.

"""

#Criando uma lista utilizando o metodo range().
lista1 = list(range(11))

#Criando uma lista utilizando string.
lista2 = list('sherek terceiro')

#Trigger em lista atravez de condição if
#Adicionar informaçoes de variaveis de maneira dinamica em string com {nome_var}
if 8 in lista1:
    print('8 esta na lista, ativar funcao.')
else:
    print('8 nao esta na lista, sem funcao.')

if 'e' in 'palavre':
    print('letra e nesta palavra')

##Listas podem ser facilmente ordenadas por ordem numerica ou alfabetica .sort().
print('string'.sort())

##Calcular o numero de correspondencias de um valor e m uma lista atravez do count.
print(lista1.count(1)) ##resultado em numero int.

##Adicionar elementos em listas, utilizamos a função append, adicionamos apenas um
##elemento por vez.
## Porem podemos adicionar um array dentro da lista Ex: append([lista]).
lista1.append(1)
lista1.append([1,2,3])

##Podemos utilizar arrays para condições.
if [5,4,3] in lista1:
    print('Econtrei a lista');
else:
    print('Nao encontrei a lista')

##extend() faz a mesma coisa que append, porem adicionar os valores individualmente cada um em
##um espaço do array, podemos adicionar multiplos valores de uma vez em uma lista.
lista1.extend([123,44,67])

##insert() inserindo em uma posição exata do array.
lista1.insert(2, "novo valor") ##na posicação 2 um novo valor.

##Unir listas.
lista3 = lista1 + lista2
lista1.extend(lista2)

##apresentar a lista ao contrario
lista1.reverse() ## Metodo
lista1[::-1] # Sintaxe

##copiar uma lista
lista3 = lista1.copy()

##tamanho da lista atravez do .len()
lista1.len()

##Remover o ultimo elemento da lista, e tambem o retorna
##podemos enviar como parametro um indice para escolher qual posicao do array quero tirar
lista1.pop()

##Limpar lista .clear()
lista1.clear()

##podemos multiplicar o conteudo dos arrays fazendo lista * numero
lista1 = lista1 * 2

##.split() transformar uma string em uma lista de palavras com .split()
##podemos definir seu separador atravez de um parametro indicando
##Ex lista1.split('.')
'string maneira'.split()

##.join(lista1) separar elementos em uma string por um parametro definido "' '"
#espaço definido como parametro.
string = ' '.join(lista1)


## Podemos misturar dados em um array.

##Iterando listas
##Ex for:
for elemento in lista1:
    print(elemento)

##Ex While
produto = ''
carrinho = []

while produto != 'sair':
    print('adicione um produto na lista ou digite "sair" para sair: ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

##acesso as posiçoes de arrays de maneiras tradicional lista1[1]
##podemos usar numeros - para acessar inversamente

##usando while com indice e length
indice = 0
while indice < len(lista1):
    indice = indice + 1

##Usando no for
for indice, item in lista1:
    print(item)

##encontrar um indice de um item na lista
print(lista1.indice("kawabanga"))

##slice lista[inicio:fim:passo]
##slice range(inicio:fim:passo)

##invertendo valores em uma lista
## ou lista1.reverse()
lista1[0], lista1[1] = lista1[1], lista1[0]

# soma da lista
sum(lista1)

# maximo valor
max(lista1)

# minimo valor
min(lista1)

#tamanho da lista len de length
len(lista1)

# transforma lista em uma tupla que é separada em () nao em []
tupla = tuple(lista1)

#desempacotamento de lista
num1, num2, num3 = lista1

#copia de lista para outra shallow copy e deep copy
#forma1 deep copy .copy() so copia os dados
listaNova = lista1.copy()

#forma2 shallow copy se modificarmos uma das listas ambas se alteram com os mesmos valores
novaLista = lista1



