from datetime import datetime as dt

hoje = dt.now()
natal = dt(2022, 12, 25, 0)

espera = natal - hoje
print(type(espera))
print(repr(espera))
print(espera)
print(f"Faltam {espera.days} dias para o natal!")

