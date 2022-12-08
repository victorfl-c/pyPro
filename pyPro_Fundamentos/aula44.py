proprietarios = {}

while True:
    apt = int(input("Informe o número do apartamento: "))
    if apt != -1:
        proprietario = input("Informe o nome do proprietário: ")
        proprietarios.update({apt:proprietario})
    else:
        break

edificio = dict(sorted(proprietarios.items()))

for chave, valor in reversed(edificio.items()):
    print(f"{chave} - {valor}")

print(f"Foram listados {len(edificio)} apartamentos.")