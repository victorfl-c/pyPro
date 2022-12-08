def area_circulo(raio):
    PI = 3.14
    area = PI * pow(raio, 2)
    return area

def area_cilindo(raio, altura):
    area = area_circulo(raio) * altura
    return area

r = float(input("Informe o raio do círculo: "))
a = area_circulo(r)
print(f"A área do círculo de raio {r} é de {a}")

h = float(input("Informe a altura do cilindo: "))
ac = area_cilindo(r, h)
print(f"A área do cilindo de raio {r} e altura {h} é de {ac}")
