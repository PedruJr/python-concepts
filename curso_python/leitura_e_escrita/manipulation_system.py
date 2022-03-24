"""
    Sistema de Arquivos - Manipulação


"""

import os

#Descobrindo se contem na pasta, serve para pastas e arquivos
#Path relativo
print(os.path.exists('./frutas.txt'))

#Path absoluto
print(os.path.exists('home/dev/frutas.txt'))

#Criar arquivos
# Podemos criar arquivos com o open e paramentro write W, logo em
#seguida podemos fechar com .close() para nao ocupar espaço na memoria
open('novo_arq.txt', 'w').close()

#Com with e pass para pular o bloco
with open('novo_arquivo.txt','w') as arquivo:
    pass

# Criar de melhor forma com os
os.mknod('new_archieve.txt')
os.mknod('home/dev/arquivos/new_archieve.txt')

#No mac este comando opera um erro, pois precisa de permissão,
#Necessitando iniciar com permissão de adm
#Caso ja exista o arquivo, retorna um erro FileExistsError

#Criando diretorio
os.mkdir('templates')
#path absoluto
os.mkdir('home/dev/templates')

#OBS se não tivermos permissão para criar o relatorio, receberemos um
#Permission error

#Criar varios diretorios ou estrutura(arvore de diretorios)
os.makedirs('homes/Xerock/templates')

#Renomear diretorios
os.rename('template/nove', 'geek2')


