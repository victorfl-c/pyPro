def num_primo(numero):
    """Função lógica que retorna True se o valor informado for primo
    Entrada: numero = numero inteiro
    Retorna: True se o número for primo, e False se não for primo"""
    if numero == 0 or numero == 1:
        return False
    else:
        qtd = 0
        for i in range(1, (numero + 1)):
            if numero % i == 0:
                qtd += 1
        if qtd > 2:
            return False
        else:
            return True

num = int(input("Informe um número: "))

if num_primo(num) == True:
    print(f"O numero {num} é primo!")
else:
    print(f"O número {num} não é primo!")
