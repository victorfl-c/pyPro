arquivo = open("texto2.txt", "r")
texto = arquivo.readlines()
print(len(texto))

print("aqui estamos trabalhando com o arquivo")
print(arquivo.closed)

arquivo.close()

print("aqui ja fechamos o arquivo")
print(arquivo.closed)