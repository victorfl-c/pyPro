from textblob import TextBlob
import datetime


def retorna_data(data):
    mes= TextBlob(data.strftime('%B')).translate(from_lang='es', to='pt-br')
    return f"{data.day} de {mes} de {data.year}"


hoje = datetime.datetime.now()
print(hoje)
hoje_formatado = retorna_data(hoje)
print(hoje_formatado)