"""
    Escrevendo em CSV

    -> Podemos escrever atravez do metodo .writer()
    -> Podemos utilizar o metodo .writerow() para escrever uma linha

"""
#importando writer/escritor
import csv
from csv import writer
#utilizamos with para fechar o open no final do bloco de codigo
#filmes.csv como arquivo a ser aberto/criado, criado neste caso
#'w' como parametro de write
# apelidade pelo 'as' como arquivo

#Metodo para escrever dados de um filme em um csv com este metodo
with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe o gênero: ')
            escritor_csv.writerow([filme, genero, duracao])


#Agora utilizando DictWriter
from csv import DictWriter

#Metodo para escrever dados de um filme em um csv com este metodo
#Semelhante ao passado
with open('DictFilms.csv', 'w') as arquivo:
    #forma de adicionar cabeçalho com DictWriter
    #Entao as chaves utilizadas devem ser iguais aos do cabeçalho
    escritorDict_csv = DictWriter(arquivo, fieldnames=['Titulo', 'Gênero', 'Duração'])
    escritorDict_csv.writeheader()#metodo para criar o cabecalho
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duracao (em minutos): ')
            escritorDict_csv.writerow({"Título: ": filme, "Gênero: ": genero, "Duração: ": duracao})

