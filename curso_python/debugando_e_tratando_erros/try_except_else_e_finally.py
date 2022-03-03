"""
Try/Except/Else/Finally

Processo simples que melhora a qualidade da aplicação.

Toda entrada de dados precisa ser tratada!

Else = Executa, Caso não de erro.

Finally = Executa sempre. Com erros ou não.
Usado para fechar ou desalocar recursos.

"""
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')
finally:
    print('Executando o finally')

############Exemplo Complexo errado

def dividir(a, b):
    return a/b

num1 = int(input('Informe o primeiro numero: '))

## A forma bagunçada, o certo seria tratar no metodo
try:
    num2 = int(input('Informe o segundo numero: '))
except ValueError:
    print('O valor precisa ser numérico')

try:
    print(dividir(num1,num2))
except ValueError:
    print('Valor incorreto')

##################

#Exemplo complexo certo

def divisor(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor Incorreto'
    except ZeroDivisionError:
        return 'Não é possivel dividir por zero'

numero1 = int(input('Informe o primeiro numero: '))
numero2 = int(input('Informe o segundo numero: '))

##Forma Generica
def divisor(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'

##Forma semi-generica
def divisor(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError):
        return 'Ocorreu um erro'