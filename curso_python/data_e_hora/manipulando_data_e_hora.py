"""
    Manipulando Data e Hora no Python

    Python possui um modulo built-in (integrado) para trabalhar com
    data e hora.
    -> import datetime


"""
import datetime#uma classe presente, podemos utilizar seus metodos

print(datetime.MAXYEAR)# até 9999

print(datetime.MINYEAR)# até ano 1

print(datetime.datetime.now)# retorna data e hora corrente, acessando a classe dentro do modulo???

print(repr(datetime.datetime.now))# Representação traz (ano, mes, day, hour, minute, second, microsecond)

#Ajustando data e hora com replace()
hora_inicio = datetime.datetime.now()
hora_inicio = hora_inicio.replace(hour=10, minute=10, second=10, microsecond=0)

#Marcando uma data e hora ano/mes/dia/hora = 2022-01-01 00:00:00
evento = datetime.datetime(2022, 1, 1, 0)

#Recebendo data do usuario e convertendo para data em python (str para datetime)
nascimento = input('Informe seu nascimento (dd/mm/yyyy): ')
nascimento = nascimento.split('/')#separar o dia/mes/ano pela
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))#separar o dia/mes/ano pela

#Acesso individual nos elementos datetime
print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)

#Descobrir os metodos possiveis print(dir())
print(dir(evento))