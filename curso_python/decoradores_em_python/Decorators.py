"""
    Decorators são funções
    Envolvem outras funções e aprimoram seus comportamentos

    Function Decorator
        - Sintaxe propria, usando "@" (Syntact Sugar/ Açucar sintatico)

"""
#Decorator como função, sintaxe sem syntact sugar, "nao recomendado"
def seja_educado(funcao):
    def sendo():
        print('Prazer conhecelo')
        funcao()
        print('Tenha um otimo dia!')
    return sendo

def saudacao():
    print('Seja bem vindo!')

#Decorando o seja_educado com outra funcao saudacao
#Funções decoradas são jogadas decorando dentro de outras funçoes
teste = seja_educado(saudacao)

##Decorators com Sintax Sugar (Açucar sintatico)
def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Prazer Conhecelo')
        funcao()
        print('tenha um bom dia!')
    return sendo_mesmo()

@seja_educado_mesmo #Sugar Syntax, decorator
def apresentando():
    print('Meu nome é Pedro')

#So precisamos chamar a funçao agora e ela ja esta usando o decorator
apresentando()

#Podemos decorar com mais @Decorators
