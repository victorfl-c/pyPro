try:
    """Ler um número inteiro"""

    num = int(input("Informe um número: "))
except:
    """Se o valor informado for diferente de um número inteiro
    retorna uma menssagem de erro"""

    print("Valor incorreto!")
else:
    """Caso o valor seja válido, imprime a menssagem e o valor"""

    print(f"Você digitou o número {num}")
finally:
    """Executa uma função, ocorrendo um erro ou não"""

    print("Fim da execução do programa!")
