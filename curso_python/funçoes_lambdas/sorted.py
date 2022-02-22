"""
Sorted

Não confundir com sort(), que so funciona em listas

Sorted ordena qualquer iteravel, criando uma nova lista como retorno
"""
#Ordenamos a lista com sort()
numeros = [4, 3, 2, 5, 6, 7]
numeros.sort()

print(sorted(numeros))#Menor para o maior

#Podemos tambem passar parâmetros
print(sorted(numeros, reverse=True))# Ordena e inverte, do maior para o menor

print(tuple(sorted(numeros)))#Menor para o maior, transformando em tupla

#Exemplo Complexo Sorted()
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolo", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amom meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Eu vou sair hoje"]},
    {"username": "Gaules", "tweets": []}
]

#Ordenação com chave padrão por len
print(sorted(usuarios, key=len))

#Ordenação com chave utilizando função lambda, por username
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

#Ordenação com chave utilizando função lambda, por tweets
#este apontara erro por conta de faltar infos no array de tweets de alguns users
print(sorted(usuarios, key=lambda usuario: usuario["tweets"][0]))


#Ordenação com chave utilizando função lambda, por quantidade de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))




