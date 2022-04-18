"""
    Métodos de datas e horas

"""
import datetime


agora = datetime.datetime.now()#agora - com now podemos especificar um timezone(fuzohorario)
hoje = datetime.datetime.today()#hoje

#Mudanças a meia noite com combine()
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())#hora 00:00:00)

#reconhecer dia da semana em int
# 0 - Segunda-Feira (Monday)
# 1 - Terça-Feira (Tuesday)
# 2 - Quarta-Feira (Wednesday)
# 3 - Quinta-Feira (Thursday)
# 4 - Sexta-Feira (Friday)
# 5 - Sabado-Feira (Saturday)
# 6 - Domingo-Feira (Sunday)
print(manutencao.weekday()) # este retorna 5 = Sabado

#Formatando datas/horas com strftime() (String Format Time)
#Desta forma sera apresentado sem as horas.
hoje.strftime('%d/%m/%Y')# Quero a formatação %d que vai me dar o dia / %m que vai me dar o mes /  %Y (MAISCULO DEVOLVE 4 digitos, minusculo apenas 2) que vai me dar o ano
#Este exemplo com "B" maiusculo recebemos uma string com  o nome do mes
hoje.strftime('%B')

#Marcando tempo de execução do codigo com