from datetime import datetime as dt

# Mostrar o dia e a hora corrente:
print(dt.now())

# Obter dados separadamente:
hoje = dt.now()
print(hoje.year)
print(hoje.month)
print(hoje.day)
print(hoje.hour)
print(hoje.minute)
print(hoje.second)
print(hoje.microsecond)
