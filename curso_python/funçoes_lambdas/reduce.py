"""
Reduce em python

Função integrada sao map e filter,
Reduce nao mais é uma função integrada, entao tempos que importar
do modulo functools.

Use reduce somente se precisa, caso contrario use loop for
È complicado de entender esta func
Recebe funcao e dados como map e filter

reduce(funcao, dados)

Dentro do reduce()
Pega os dois primeiros dados e preenche uniforme na funçao resignada
resultado1 = funcao(parametro1, parametro2) #aplica a funçao nos dois primeiros elementos da coleção
e armazena o resultado.

Apos isso ele vai pegar o resultado final e usalo na funçao com o prox dado da lista interavel enviada como parametro
Isso é repetido ate o final da lista

Alternativamente reduce() é
funcao(funcao(funcao(p1,p2),p3),p4),  ...)
"""
from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 25]

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

#forma normal
resultado = 1
for n in dados:
    resultado = resultado * n

print(resultado)

