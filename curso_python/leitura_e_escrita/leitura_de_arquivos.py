"""
    Leitura de Arquivos

    Utilizamos a função integrada open() "abrir"

    Na forma mais simples passamos apenas um parametro ao open()
    o nome do arquivo a ser lido, esta função RETORNA um arquivo
    __io.textIOWrapper e é com ele que trabalhamos

    por padrão a função open() abre o arquivo para leitura,
    caso nao encontre, RETORNARA FileNotFoundError


"""

#Este abre o arquivo, é necessarioo outro metodo para leitura
arquivo = open('texto.txt')

##Mostrara as especificações do arquivo name, mode, encoding. class _io.TextIOWrapper
## Mode= 'r' = somerte leitura -> read()
# encounding = 'UTF-8'
print(arquivo)

##Apos abrir o arquivo, este metodo le o arquivo
## Metodo de leitura funciona a partir de um cursor que começa no
## Inicio do texto e ao terminar leva o cursor para o final do texto

## READ() LE TODO CONTEUDO DO ARQUIVO PROFESSOR LOOUCO
print(arquivo.read())

