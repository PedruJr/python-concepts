"""
    StringIO -> Utilizado para ler e criar arquivos em Memória

    ATENÇÂO: ler ou escrever dados em arquivos no sistema é necessario
    permissão do sistema de leitura e escrita.


"""

from io import StringIO

mensagem = "Stringn normal"

#Criar o arquivo em memoria, sem conteudo pode se adicionar o conteudo depois.
#Com conteudo, cria com o conteudo, podemos entao tratar a string como arquivo
# arquivo = open('arquivo.txt' 'w')
# print(arquivo.read())
# arquivo.seek(0))
arquivo = StringIO(mensagem)

