from datetime import date as dt

# Receber uma string e transformar em datetime:
nascimento = input("Entre co ma data (dd/mm/aaaa): ")
# Guardar cada valor (dia,mês e ano) em uma posição da lista
nasc_list = nascimento.split("/")
nasc_data = dt(
    int(nasc_list[2]),
    int(nasc_list[1]),
    int(nasc_list[0])
)
print(nasc_data)
print(type(nasc_data))
