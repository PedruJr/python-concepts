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
#Caso diretorio nao exista, retorna um FileNotFoundError
#Se o diretorio não estiver vazio, retorna um OSError
os.rename('template/nove', 'geek2')
os.rename('path/path/fileNameChange.txt', 'path/path/NameChanged.txt')

#Deletar ARQUIVOS APENAS, ao realizar este delete não vai para lixeira
#No windows não permite deletar arquivos ou processos em uso
#Caso arquivo não exista, FileNotFoundError
#Caso seja um diretorio e não um arquivo, erro de IsADirectory
os.remove('path/path/fileNameChange.txt')

#Remover DIRETORIOS apenas vazios, com conteudo dentro retorna um erro IsNotEmpty
os.rmdir('path/directory')

#Remover arvore de diretorios com conteudos dentro combinando as funçoes
for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)

#Remover de forma pythonica diretorios vazios
os.removedirs('path/path/directorys')

#Podemos baixar uma biblioteca chamada send2trash para enviar para a lixeira
#possibilitando a restauração

#Arquivos e Diretorios temporarios.
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporariro.txt'), 'w') as arquivo:
        arquivo.write('Geek \n')
        input()

# Criando um diretorio temporario, entrando nele e criando um arquivo escrevendo um texto
# Usamos um input para manter os arquivos temporarios vivos dentro do bloco with
# Em arquivos temporarios so conseguimos escrever bits, por isso b antes da string, para converter
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek\n')
    print(tmp.read())