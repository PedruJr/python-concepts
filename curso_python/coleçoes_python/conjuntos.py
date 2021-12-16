"""
Conjuntos

- Conjuntos nas linguagens de programação se refere a teoria dos conjuntos
em matematica.

- sets (conjuntos nao possuem valores duplicados)
- sets (não possuem valores ordenados)
- elementos nos sets não são indexados

Conjuntos são bons para quando precisamos armazenar elementos,
mas não nos importamos com a ordenação deles, ou com chavez, valores
e itens duplicados

os conjuntos sets são referenciados por {} como os dicionarios/mapa
- diferença entre dicionario e um set/conjunto
    - dicionario tem chave e valor
    - conjunto tem apenas valor
"""
#definindo um conjunto:

#forma 1 com metodo set
#valores repetidos são ignorados sem gerar erro

s = set({ 1, 2, 3, 4, 5, 6, 9, 9, 2, 3})

#forma 2 a mais comum
ss = {1, 2, 3, 4, 5, 6, 6}

#podemos utilizar o metodo set em strings, transformando cada letra em
#espaço do conjunto como um item da lista, alem disso

#podemos tambem listar uma lista sem valores repetidos usando o metodo nativo
#set(lista)
#podemos saber a quantidade de elementos unicos combinando set e len

#lembrar que sets/conjuntos nao possuem valor repetido

#REMOVER ELEMENTOS DO CONJUNTO/SET
#apontamos o valor do elemento a ser removido
ss.remove(1) # não é o indice/posição, pois conjuntos nao sao indexados

#segunda forma
ss.discard(2)

##COPIANDO DEEP COPPY
novo = s.copy()

##COPIANDO SHALLOW COPPy
novo1 = ss

##REMOVENDO TODOS OS ITENS COM CLEAR()
novo.clear()

#Metodos matematicos dos conjuntos

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilheme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

#conjunto concatenar conjuntos
#utilizando UNION()
## Segunda forma atravez do | Exemplo: conjunto3 = estudantes_python | estudantes_java
estudantes_dos_dois_cursos = estudantes_python.union(estudantes_java)

##Forma de criar um conjunto somente com os elementos em comum das listas
##Atravez do intersection
ambos = estudantes_python.intersection(estudantes_java)

##apenas os valores que nao estao em ambos conjuntos
##utilizando .diference()
diferença_estudantes = estudantes_python.difference(estudantes_java)
