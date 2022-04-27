"""
    Meta data

"""
from importlib import metadata
#podemos obter informações do sistema
#Exs:
print(metadata.version('pip'))#Versao

metadados_pip = list(metadata.metadata('pip'))#Todos os metadados

print(metadados_pip['Project-URL'])# Acessando metadados em lista

print(len(metadata.files('pip')))# Quantos arquivos em pip

print(metadata.requires('pip'))#o que necessita para instalar o pip

