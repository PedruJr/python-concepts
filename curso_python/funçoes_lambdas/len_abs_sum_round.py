"""
Len, Abs, Sum e Round

#len - retorna o nunero de items em um iteravel
"""
print(len('Geek University'))

# por de baixos dos panos, dunder len é o nome dos __ __
# Aprenderemos que podemos modificar func dunder para nossas necessidades
print('Geek University'.__len__())

# Exemplo Abs, que retorna somente o valor sem o sinal, caso seja positivo ou negativo
# Não podemos utilizar na String este
print(abs(-5))
print(abs(5))
print(abs(-5.5))
print(abs(5.5))

# sum podemos passar um parametro extra a ser somado ao iteravel,
print(sum([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5], 5))

#Round ->> retorna um numero arredondado apos um numero quebrado, caso nao tenha inteiro
#Retornara o numero mais proximo do inteiro
print(round(2.5))
