"Manipulação de arquivos"

#Abrir arquivo txt com parâmetro 'r'(leitura
arquivo = open("texto.txt","r")
print(type(arquivo)) #io.TextIOWrapper
#Inserir a leitura do arquivo txt na variável texto
texto = arquivo.read()
#Imprimir o conteúdo inserido na variável texto
print(type(texto))
print(texto)

arquivo.close()
