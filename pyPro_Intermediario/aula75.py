#Abrir o arquivo texto.txt com parâmetro de escrita("w")
arquivo = open("texto.txt", "w")
#Ler o texto que será inserido na variável texto
texto = input("Digite um texto: ")
#Inserir o conteúdo da variável texto na variável arquivo
arquivo.write(texto)
#Fechar edição de arquivo
arquivo.close()
