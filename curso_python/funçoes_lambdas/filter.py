"""
Filters em python

filter -> Filtra dados de uma coleção


"""
##Calculando media pythonicamente
valores = 1, 2, 3, 4, 5

media = (sum(valores)/len(valores))

print(media)

#Biblioteca para trabalhar com dados estatisticos
import statistics

#dados vindos de um sensor
dados = [1.3, 2.7, 0.8, 4.3, -0.1]

#calculado a media utilizando a funçao statistics.mean()
media = statistics.mean(dados)

#OBS: Assim como o map(), filter() recebe tambem dois parametros,
#Uma funçao e um parametro iteravel
#Filtro trabalha com true ou false, true é filtrado, false não é

res = filter(lambda valor: valor > media, dados)
print(list(res))
#Este retorna um dado Filter Object

##Fica na memoria ate ser usada como map, limpa a memoria
print(f'Novamente: {list(res)}')

#Filter usado para identificar dados faltando,
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

#Remove os dados em branco!
resultado = filter(None, paises)

#Em lambda
results = filter(lambda pais: len(pais) > 0, paises)

#Exemplo Complexo
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolo", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amom meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Eu vou sair hoje"]},
    {"username": "Gaules", "tweets": []}
]

#Forma 1
usuarios_inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

print(usuarios_inativos)

#Forma 2 verificando com not, verifica se tem conteudo dentro do especificado
inativos = list(filter(lambda usuario: not usuario['tweets'] == 0, usuarios))

#Combinando filter e map
nomes = ['Vanessa', 'Ana', 'Maria']

#Devemos criar uma lista dizendo o nome da sua instrutora,
#Sua instrutora precisa ter 5 letras no nome ou menos

#chamamos o filter para filtrar o dado que entra como parametro no map
nome_instrutora = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(nome_instrutora)
