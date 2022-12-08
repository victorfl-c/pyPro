def fruta(n):
    lista = ["abacaxi", "banana", "melão", "maçã"]
    if n > 3:
        raise IndexError("O valor excede o número de elementos da lista!")
    else:
        return (lista[n])

n = int(input("Informe um valor:"))
print(fruta(n))