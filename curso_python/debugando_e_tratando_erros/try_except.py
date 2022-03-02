"""
Utilizamos Try/Except para tratar erros que podem ocorrer no nosso código. Previnindo
que o sistema para de funcionar retornando mensagens de erros inesperadas

Modelo:
try:
    // Execução problemática
except:
    // o que devera ser feito caso de problema

"""
#Exemplo1 - Tratando erro genérico

try:
    geek()
except:
    print('Deu problema')

##Melhor forma de tratar erros e de forma especifica, usando os TiposDeErros
#Caso Apontamos o tipo de erro errado, estourara outro tipo de erro.
try:
    geek()
except NameError:
    print('Voce esta utilizando uma função inexistente')

#Apontando a mensagem de erro junto com o tratamento
#Assim Podemos gravar no log
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

#Tratando multiplos tipos de erros
#Assim Podemos gravar no log
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')
except NameError as erra:
    print(f'Deu NameError: {erra}')
except:
    print(f'Erro Generic')

#Tratando erros em metodos
def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return print('Chave invalida')

dic = {"nome": "geek"}

print(pega_valor(dic, "game"))

