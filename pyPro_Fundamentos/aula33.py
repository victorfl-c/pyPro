#Ler o valor de um ano e verificar se é bissexto ou não
ano = int(input("Informe o ano: "))
if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")