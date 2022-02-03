"""
Entendendo o *args

Ele é um parametro como outro qualquer, podemos chamar de qualquer nome,
só precisa iniciar com o * ex: *xis, mas por convenção definiram como args

*args, este parametro utilizado em uma função, valores extras sao colocados em uma tupla imutalvel

no caso do metodo receber mais parametros que o especificado ex:def soma_todos_numeros_com_args(*args):

"""

def soma_de_numeros(num1, num2, num3):
    return num1 + num2 + num3

##função com args
def soma_todos_numeros_com_args(*args):
    total = 0
    for numero in args:
        total = total + numero
        return total

soma_todos_numeros_com_args(1, 2, 3) #isso funciona

def verificar_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'nenhum parametro reconhecido'