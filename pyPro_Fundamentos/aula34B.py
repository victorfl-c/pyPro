#Calcule o peso ideal de uma pessoa de acordo com o sexo

#Inicia a variável para receber o peso ideal
pesoIdeal = 0
#Ler a altura
h = float(input("Informe o sua altura: "))
#Ler o sexo
print("Informe o seu sexo: ")
print("1 - Masculino")
print("2 - Feminino")
sexo = int(input("Opção: "))
#Verificar se o sexo é masculino
if sexo == 1:
    #Caso a opção seja '1', o peso ideal recebe o peso ideal Masculino
    pesoIdeal = (72.7 * h) - 58
    #Imprimir o peso ideal masculino
    print("Seu peso ideal é:", pesoIdeal)
#Verificar se o sexo é Feminino
elif sexo == 2:
    # Caso a opção seja '2', o peso ideal recebe o peso ideal Feminino
    pesoIdeal = (62.1 * h) - 44.7
    #Imprimir o peso ideal Feminino
    print("Seu peso ideal é:", pesoIdeal)
else:
    print("Digite '1' para Masculino ou '2' para Feminino!")


