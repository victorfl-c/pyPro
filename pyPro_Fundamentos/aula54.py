"""Quando não sabe-se quantos parâmetros serão informados,
utiliza-se o *args, que retorna uma tupla"""
def soma(*args):
    return sum(args)

print(soma(1,6,4,9))

"""**kwargs retorna os os elementos de chave e valor,
dentro de um dicionário"""

def comida_favorita(**kwargs):
    for chave in kwargs:
        print(f"{chave} gosta de {kwargs[chave]}")

comida_favorita(victor="pizza",idrielle="pudim",mariza="bolo")