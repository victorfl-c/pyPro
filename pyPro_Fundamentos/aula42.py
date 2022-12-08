cidades = []
FIM = "sair"
resp = ''
qtd = 1

while resp != FIM:
    resp = input(f"Informe o nome da {qtd}ª cidade: ")
    qtd += 1

    if cidades != FIM:
        cidades.append(resp)
        cidades.sort()

for i in range(0, len(cidades)):
    print(cidades[i])

#CÓDIGO DO PROFESSOR PIVA:

'''
cidades = []

while True:
    print("Digite uma cidade: ")
    if cidade == sair:
        break
    else:
        cidades.append(cidade)
        
if len(cidades) > 0:
    cidades.sort()
    
    for cidade in cidades:
        print(cidade)

else:
    print("A lista de cidades está vazia")
'''
