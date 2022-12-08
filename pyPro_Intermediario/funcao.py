def primo(n):
    '''Retorna True se não for primo
    e False caso contrario.
    n deve ser um número inteiro maior que 1'''
    eprimo = True
    qtd_div = 0
    for i in range(1, n):
        if (n % 2) == 0:
            qtd_div += 1

    if qtd_div > 1:
        eprimo = False

    return eprimo
