try:
    pypro()
except NameError:
    print("Utilização de função inexistente!")

try:
    len(9.36)
except TypeError as erro:
    print(f"A aplicação gerou o seguinte erro: {erro}")

def retorna_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dicio = {"Nome":"Victor"}
print(retorna_valor(dicio, 5))
