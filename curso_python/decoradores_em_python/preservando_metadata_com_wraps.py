"""
    Preservando Metadata com Wraps

    Metadata -> sao detalhes do arquivo, como tamanho, ultima modificação,
    infos intrisecas, nao aparentes.

    Wraps -> Funções que envolvem elementos com diversas finalidades


"""
#Import para fazer parametros do decorator nao trocarem
from functools import wraps

def ver_log(funcao):
    @wraps(funcao)#Prezerva os meta dados de documentaçção
    def logar(*args, **kwargs):
        """Função dentro de outra - Decorator"""
        print(f'aqui voce esta chamando {funcao.__name__}')
        print(f'aqui voce esta chamando {funcao.__doc__}')
        return funcao (*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois numeros."""
    return a + b

#documentos ficam alterados mandando a doc de ver_log não do soma
#wrap mantem a doc para a função que tiver sido usada como decorator

print(soma.__name__)
print(soma.__doc__)
