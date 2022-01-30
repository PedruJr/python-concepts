"""
Funções em python - definindo funões

pequenos ou grandes escopos/partes de codigo com funções/tarefaz
especificas

podem ou nao retornar algum dado

pode ser executado multiplas vezes

uma função que realiza varias funçoes dentro dela precisa ser
simplificada

"""

"""
Definindo uma Função em python:

def nome_da_funcao(parametros):
    bloco_da_funcao

funçoes sempre com letras minusculas e por underline Snake case

parametros podem ser opcionais, mesmo apontados podem ser opcionais
bloco da funçao pode se r chamado de corpo ou implementação, onde ocorre o processamento
pode ou nao ter um retorno

def é utilizado para definir uma função e abrimos o bloco de codigo com : e identaçao
"""

def diz_oi():
    print('oi')

#utilizando/chamada da função
diz_oi();

#utilizando a funçao varias vezes
for numero in range(5):
    diz_oi()

#podemos atribuir uma função a uma variavel, e executala
dizeroi = diz_oi()