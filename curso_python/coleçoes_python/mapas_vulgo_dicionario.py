"""
Mapas -> tambem conhecidos como dicionarios
Representados por -> {}
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}

#Iterando com dicionarios
#Mostrar a chave no dicionario
for chave in receita:
    print(chave)

#Mostrar o valor passando a chave
for chave in receita:
    print(receita[chave])

#Mostrando com string dinamica
for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

#utilizando metodos para mostrar todas as chaves
print(receita.keys())

#utilizando metodo para mostrar os valores
print(receita.values());

#desempacotamento de dicionarios, atravez de metodo, passando dois parametros no for
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

#Podemos fazer soma, Valor maximo, valor minimo e tamanho
#Caso sejam numeros sum, max, min e len que sao metodos nativos python