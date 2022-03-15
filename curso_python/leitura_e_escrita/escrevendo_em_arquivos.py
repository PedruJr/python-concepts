"""
    Escrevendo em arquivos

    1° - Abrir com open, em um formato alternativo, o original abre
    somente para leitura.

    2° - Então apos usar o  open('arq.txt', 'w') depois usamos o
    .write('Escrita do arquivo')

    3° - Abrir um arquivo para escrita com W de write, caso tenha um nome
    de arquivo ja existente, ele apaga o conteudo do arquivo e substituido.


"""

## Exemplo de arquivo de escrita - modo 'W' de writte provavel
## Ao abrir um arquivo com 'W' de escrita, o arquivo tbm é criado no sistema

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivos. \n')
    arquivo.write('Mais uma linha. \n')

##Condição para anotar uma lista de frutas
with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe sua fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
        else:
            break
