import datetime

def dia_da_semana(valor):
    dia = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
    return dia[valor]


hoje = datetime.datetime.now()
amanha = hoje + datetime.timedelta(days=1)

meia_noite = datetime.time()

tarefa = datetime.datetime.combine(amanha, meia_noite)
print(type(tarefa))
print((repr(tarefa)))
print(tarefa)
print(dia_da_semana(tarefa.weekday()))