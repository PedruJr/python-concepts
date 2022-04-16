"""
    Lendo arquivos CSV

    CSV - Comma Separeted Values - Valores separados por virgula
        OBS: podem ser usado outros separadores, por ponto e virgula tambem como exemplo
        Pode ser usado espaço, o ideal é manter o padrão dos separadores

    Arquivo lutadores.csv -> Arquivo exemplo, nem sempre temos o cabeçalho apontando
        os valores das colunas.

    A linguagem python possui duas formas para ler csv com modulos nativos:
     Reader -> Iteramos as linhas do arquivo csv como lista
     DictReader -> Iteramos as linhas como ordered list
     OBS: por padrão utilizam a virgula como delimitador, podemos passar
        o parametro secundario (xxxx, delimiter = ';') para setar o delimitador

"""
               ####POSSIVEL POREM NÂO O IDEAL + TRABALHOSO###
#Exemplo com o arquivo dentro da pasta onde estamos com nossa aplicação python
#Abrindo o csv como arquivo
with open('lutadores.csv') as arquivo:
    #colocado os dados do arquivo em uma variavel com .read()
    dados = arquivo.read()
    #utilizando .split(valorDoSeparador) para segregar as infos do arquivo
    #Para não pegar as infos do cabeçalho ou pegar so as infos do cabeçalho,
        #Utilizamos Slice[2:] pulamos  a posição 0, 1 ,2 do cabeçalho
        #entao pegamos o resto dos dados
    dados = dados.split(',')[2:]
    print(dados)

# Reader CSV
from csv import reader
with open('lutadores.csv') as lutadores:
    leitor_csv = reader(lutadores)
    #Ex: com outro delimitador     leitor_csv = reader(lutadores, delimiter = ',')
    #Iteradores podemos utilizar para pular a primeira linha de cabeçalho:
    next(leitor_csv)# Pulamos a primeira linha, a linha de cabeçario
    #cada linha vira uma lista
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros')

# DictReader
from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        #Cada linha é um orderedDict, acessamos os elemtos pelo nome da chave
        #Não precisamos dar um next devido a puxar os valores pelas chaves
            #Ordered dict usa o cabeçalho para montar CHAVE e VALOR
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura em (em cm)']}")

