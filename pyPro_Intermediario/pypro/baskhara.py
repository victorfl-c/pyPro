import math


def main():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    imprime_raizes(a, b, c)


def delta(a, b, c):
    return b ** 2 - 4 * a * c


def imprime_raizes(a, b, c):
    if delta(a, b, c) == 0:
        raiz = (-b + math.sqrt(delta(a, b, c))) / (2 * a)
        print(f"A única raiz é: {raiz}")
    else:
        if delta(a, b, c) < 0:
            print("Esta equação não possui raízes reais!")
        else:
            raiz1 = (-b + math.sqrt(delta(a, b, c))) / (2 * a)
            raiz2 = (-b - math.sqrt(delta(a, b, c))) / (2 * a)
            print(f"\nX1: {raiz1} X2: {raiz2}")

