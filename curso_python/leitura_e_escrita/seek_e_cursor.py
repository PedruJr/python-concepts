"""
    Seek e Cursores

    seek() -> Movimenta o  cursor no arquivo, para aplicar o read()

"""

#Apos open() e read() o arquivo, utilizamos seek(0) para retornar o cursor

arquivo = open('texto.txt')

print(arquivo.read())

#Retornando o cursor ao inicio
# Cada caracter é uma posiçao no seek
arquivo.seek(0)

# Ler somente uma linha, devolve uma string que podemos utilizar os metodos do tipo de dado
readOneLine = arquivo.readline()

#separar as palavras por ' ' em uma lista
print(readOneLine.split(' '))

#Podemos tambem ler todas as linhas com o readlines() note o S no final

## Open vincula o arquivo com o disco do computador chamado de Streaming
## Ao finalizar o trabalho com o arquivo fechamos este streaming com o close()

arquivo.close()

##Podemos limitar o read por caracters indicando um int como parametro
arquivo.read(50)

