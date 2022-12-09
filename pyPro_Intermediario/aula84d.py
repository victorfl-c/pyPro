import datetime as dt

def retorna_data(hoje):
    meses = ['', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    return f"{hoje.day} de {meses[hoje.month]} de {hoje.year}"

# Mostrar horas formatadas: Método strftime()
hoje = dt.datetime.now()
print(hoje)
hoje_formatado = hoje.strftime('%d/%m/%y')
print(hoje_formatado)
hoje_formatado = hoje.strftime('%d/%B/%y')
print(hoje_formatado)
hoje_formatado = retorna_data(hoje)
print(hoje_formatado)
