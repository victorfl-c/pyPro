import datetime

hoje = datetime.datetime.now()
amanha = hoje + datetime.timedelta(days=1)

meia_noite = datetime.time()

tarefa = datetime.datetime.combine(amanha, meia_noite)
print(type(tarefa))
print((repr(tarefa)))
print(tarefa)