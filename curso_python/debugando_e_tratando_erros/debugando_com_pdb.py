"""
Debugando com PDB

PDB -> Python Debugger

Bug -> Inseto

Utilizar print() para debbugar é uma pratica ruim, pois existem maneiras melhores.
Em python utilizamos  diferentes IDES ou o PDB
"""

#Exemplo com o Pycharm, atravez de breakpoints:
def divirdir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro: {err}'

#Utilizando o Python Debugger, precisamos importar a biblioteca pdb
#E então utilizar a função set_trace()
#Comando basicos PDB
# l (Listar onde estamos)
# n (Proxima linha)
# p (Imprime variavel)
# c (continua a execução - finaliza o debug)
# p + nome var (Para imprimir).
# Escrever o nome da var aponta seu conteudo

#A partir do python 3.7 não é mais necessario imoprtar o pdb
#podemos utilizar a função integrada chamada breakpoint()

#podemos imoprtar e usar o metodo com ; apos importar
import pdb; pdb.set_trace();

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
breakpoint(); # = pdb.set_trace();
nome_completo = nome + ' ' + sobrenome
curso = 'Programação essencial em python'
final = nome_completo + 'Faz o curso' + curso
print(final)