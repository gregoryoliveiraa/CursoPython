#
# Arquivo com exemplos de manipulação de  datas
#

from datetime import date
from datetime import time
from datetime import datetime

def ManipulandoDAtaHora():
    hoje = date.today()
    print("Hoje é: ", hoje)
    print("Partes da data: ", hoje.day, hoje.month, hoje.year)
    print("Numero do dia da semana", hoje.weekday())
    dias = ["Dom", "Seg", "ter", "Quar", "quint", "sex", "sabado"]
    print("Dia", dias[hoje.weekday()])

    data = datetime.now()
    print("Data e hora:", data)

    datetime.hour()
    print
ManipulandoDAtaHora()