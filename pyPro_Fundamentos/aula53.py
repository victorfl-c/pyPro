def potencia (numero, expoente = 2):
    """Função que calcula a potência de um número
    Valores de entrada:
    numero - número a ser calculado(elevado a potencia)(float)
    expoente - expoente a ser utilizado no calculo (inteiro)

    Valor de saída:
    resultado - resultado do calculo da potência (float)
    """
    resultado = pow(numero, expoente)
    return resultado

n = float(input("Informe o número: "))
e = int(input("Informe o expoente: "))

print(f"valor com expoente: {potencia(expoente=e,numero=n)}") #parâmetros invertidos
print(f"valor sem expoente: {potencia(n)}") #Utilizando parâmetro padrão (expoente)
print("----------------------------------")
help(potencia)