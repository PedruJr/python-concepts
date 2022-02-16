"""
Listas Aninhadas (Nested List)

-Algumas linguagens tem estruturas de dados chamadas arrays
    - Unidimensionais(Arrays/Vetores);
    - Multidimensionais(Matrizes);

- Em python sao as listas

numeros = [1, 2, 3, 4, 5,]

"""

#Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #Matriz 3x3

#Acessando os dados
print(listas[0])

#lista 0 coluna 2
print(listas[0][1])

#lista 2 coluna 2
print(listas[2][2])

#Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)

#com list comprehension
[[print(valor) for valor in lista] for lista in listas]

#Gerando um tabuleiro/matriz 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

#Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else '0' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

