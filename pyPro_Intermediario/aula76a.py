#Primeira forma
arquivo = open("texto2.txt")
texto = arquivo.read()
#imprimir o arquivo linha por linha
for linha in texto.splitlines():
   print(linha)

arquivo.close()
#Segunda forma
arquivo = open("texto2.txt")

for linha in arquivo:
   print(linha)

#Retornar o cursor para a posição 0
arquivo.seek(0)

for linha in arquivo:
   print(linha.strip())#strip() remove os espaços vazios

arquivo.close()
