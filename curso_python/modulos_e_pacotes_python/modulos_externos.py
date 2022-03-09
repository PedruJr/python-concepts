"""
    Modulos Externos

    Utilizamos o pip gerenciador de pacotes - Python Installer Package

    https://pypi.org - todos os pacotes e externos

    Ex:
    pip install colorama -> utilizado para textos coloridos no terminal

    Att pip:
    pip install --upgrade pip
"""
from colorama import init, Fore

init()

print(Fore.MAGENTA + 'Geek University')
print(Fore.BLUE + 'Geek University')

import pydf
pdf = pydf.generate_pdf('<h1>Geek University</h1>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)