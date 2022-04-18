"""
    Deltas de data e hora

    -> Diferença entre duas datas (chamamos de delta)

"""
import datetime

#data de hoje
data_hoje = datetime.datetime.now()
#data de algum evento futuro
aniversario = datetime.datetime.now()
#calculando o  delta entre os dois
tempo_para_evento = aniversario - data_hoje
print(type(tempo_para_evento))# tipo da variavel
print(repr(tempo_para_evento))# apresentação detalhada em python
print(tempo_para_evento)# dias e horas ate o evento

#Como utilizamos objetos python datetime, podemos acessar seus atributos da classe
print(f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 60}') # lembramos que podemos utilizar // para retornar uma divisao inteira

#Setando diminuição/adição de dias em variaveis atravez de timedelta()
regra_boleto = datetime.timedelta(days=3) # dias as serem diminuidos
data_compra = datetime.datetime.now()# dia atual
vencimento_boleto = data_compra + regra_boleto
print(vencimento_boleto)
