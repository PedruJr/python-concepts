"""
Dicionarios python, em outras linguagens sao chamadas de mapas.

    -> È um conjunto com uma relação entre chave x valor.
    -> Diferente da lista que possui apenas valor, apesar de seus valores possuir
um index.
    -> O dicionario possui a chave explicita e não implicita.
    -> Dicionarios sao representados por chaves type({}), como os sets(conjuntos).
    a diferença é que sets não utilizam chave ou um index.
"""
#Definindo dicionarios
#Sintaxe: dict = {chave:valor, chave:valor}
#OBS: Podem ser de qualquer tipo de dado, tambem é possivel misturar os dados.
paises = {'br':'Brasil', 'eua':'Estados Unidos', 'py': 'Paraguai'}

#Para acessar os elementos
#Forma 1 - por conchetes e o valor da chave
paises['br']

#Forma 2 - por get, forma recomendada.
#Podemos passar um segundo parametro que sera dado como resultado.
#caso não encontre a chave passada como paramentro.
paises.get('br', 'pais nao encontrado')

#saber se esta dentro da lista, podemos saber se tem com a key.
#'in' retorna true ou false.
print('br' in paises)

#usando condição de tem em dicicionario (dict)
if 'ru' in paises:
    russia = paises['ru']

#Podemos usar qualquer tipo de dado tambem em um dicionario {}

#outra forma de criar um dicionario
paises = dict(br='Brasil', eua='Estados Unidos', py="Paraguay")

#Outro exemplo de dicionario com valores compostos.
#Podemos passar valores multiplos como chave.
#Tuplas tem uma boa funcionalidade como chaves por serem inalteraveis.

localidades = {
    (35.9924, 39.8917): 'Escritorio em Tókio',
    (35.9864, 39.2134): 'Escritorio em Vegas',
    (35.5435, 39.5436): 'Escritorio em Portugol',
}


#Adicionando informações ao dicionario por conchetes
localidades[(35.7643, 39.4352)] = 'Escritorio Narnia'

#Adicionando informaçoes com dict.update(novoDicionario).
#Ex:
novaLocalidade = {(22.2345, 39.4321) : 'Escritorio Narnia'}

localidades.update(novaLocalidade)

#atualizamos parecido com a inserção, parece um javascript adicionando informação a um objeto
#tambem atualizamos utilizando o update e o valor da chave que queremos alterar
#Não repetir as chaves.

#Removendo um elemento atravez do .pop('chave do valor a ser removido').
#Sempre passando a chave do valor a ser removido.
#Ao remover o objeto, o seu valor é retornado.
localidades.pop(novaLocalidade)

#Removvendo por del.
del localidades[(22.2345, 39.4321)]
#Desta forma o valor nao é retornado.
#um dicionario funciona como um json, chaves com seus valores dentro.
carrinho = []
produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'Deus da Guerra 4', 'quantidade': 1, 'preço': 300.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

#Limpando o dicionario
localidades.clear()

#copiando um dicionario para outro
#Deep copy
localidades2 = localidades.copy()

#Shallow copy, aponta para o mesmo lugar da memoria, são o mesmo objeto
localidade3 = localidades

#forma nao usual de criar dicionarios
outroDicionario = {}.fromkeys('a','b')

#defininindo uma lista de chave e o atributo destas chaves
usuario = {}.fromkeys(['nome','pontos','email', 'profile'], 'desconhecido')

#desta forma cada letra vira o valor da chave com o seu valor
veja = {}.fromkeys('teste', 'valores')

