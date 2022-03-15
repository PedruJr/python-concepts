"""
    O bloco with

    Para trabalhar com arquivos:

    1° - Abrimos o arquivo
    2° - Manipulamos o arquivo
    3° - Então fechamos o arquivo devido, ao processo de streaming
    que fica aberto ao abrir um arquivo de texto.

    O bloco with é utilizado para criar um contexto de trabalho,
    onde os recursos utilizados sao fechados apos a utilização

"""

# Bloco with com contexto, abre e fecha para nos o arquivo
# Forma pythonica de mexer com arquivos
with open('texto.txt') as arquivo:
    print(arquivo.readlines())


