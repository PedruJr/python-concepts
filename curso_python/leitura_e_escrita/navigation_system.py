"""
    Navigation System - OS Module (Operation System)

    First, you need to import the OS module, to manipulate
    system files
"""
import os

#Metodos OS

# os.getcwd() -> Returns file absolute-path
import sys

print(os.getcwd())

# os.chdir('') -> Change directory
# returning to previous dir
os.chdir('..')

#checking dir, to check chdir
print(os.getcwd())

#Checar se o path e absoluto ou relativo
# Caso seja usuario windows necessario aplicar duas contra barras \\
# Ex: 'C:\\Users\\Tiao'
# No caso do linux / apenas uma barra normal
# Ex: '/home/dev/'
print(os.path.isabs(''))

#Identificando SO (Posix ou nt) com os.name
print(os.name) # posix(Linux e mac), nt (Windows)

#Mais detalhes do SO
print(os.uname())

## Identificando real SO - linux ou windows
print(sys.platform)

##desenvolvendo um caminho usando getcwd no caminho atual + os.path.join
## e então passamos o caminho final como segundo parametro
## Este metodo se adapta ao sistema operacional na hora de montar a rota
## devido aos caminhos windows dividir por contra barra \
## Alem disso podemos passar outros parametros apos o segundo e agregar
## mais pastas ainda ao endereço
caminho = os.path.join(os.getcwd(), 'geek', 'university')

##Entao usamos o caminho desenvolvido com os.chdir(caminho)
os.chdir(caminho)

## Listar diretorios e arquivos
## podemos passar um path por parametro, como /etc ou a propria var caminho
print(os.listdir())

#Mais detalhados com os.scandir('caminho')
##È necessario fechar o scandir, recomendado usar com with
## Ou então scanner.close
## podemos utilizar list para ter uma var com as infos
arquivos = list(os.scandir('caminho'))

#acessando os arquivos da lista e executando metodos nativos
arquivos[0].is_dir()
arquivos[0].is_file()
arquivos[0].is_simlink()#Link simbolico
arquivos[0].name()
arquivos[0].path()
arquivos[0].stat() # Estatisticas
