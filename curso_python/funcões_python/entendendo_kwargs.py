"""
Compreendendo Kwargs
podemos chamar de duplo **xis, por convenção chamamos de **kwargs

o Kwargs exige que utilezemos parametros noemados que se transformam
em dicionarios = chave e'valor'

"""
##Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

##Exemplo2

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythonico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return "Não tenho certeza de quem você é ..."

"""
#Ordem de parametros em funções
- Parametros obrigatorios
- Args
- Parametros default (não obrigatorios)
- Kwargs
"""

#Exemplos de paremetrização com ordem correta

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('casado')
    print(kwargs)

minha_funcao(19, 'carlos', 3, 2, 1, solteiro=True, python=True)

#utilizando * para desempacotar args e kwargs
#Desempacotar **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Johnson', 'sobrenome': 'Wayne'}

#utilizando ** antes da chave com valor (dicionario) para desempacotar
print(mostra_nomes(**nomes))

#podemos utilizar em outros desempacotamentos Ex
lista = [1, 2, 3]

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

#desempacotado com sucesso utilizando asterisk
#Ex: soma_multiplos_numeros(*lista)

#podemos desempacotar tuplas e sets com * tambem
#lista = [1,2,3]
#tupla = (1,2,3)
#conjunto/set = {1,2,3}
#dicionario = dict(a=1, b=2, c=3) este desempacotamos com duplo ** asterisk

#Obs o dicionario precisa ter suas chaves com mesmo nome dos parametros ao ser utilizado
#como um parametro


