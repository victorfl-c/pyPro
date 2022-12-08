#Set comprehension
conjunto = {num for num in range(1, 7)}
print(conjunto)
quadrado = {num**2 for num in conjunto}
print(quadrado)

#Gerando um conjunto de caracteres extraídos de uma frase
frase = "pyPro - Seja um profissional Python!"
letras = {letra for letra in frase}
print(letras)
