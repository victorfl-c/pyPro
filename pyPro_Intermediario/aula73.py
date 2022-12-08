'''Desafio - Criar uma nova lista de produtos
com os valores com desconto de 5%'''

lista_produtos = {
    "geladeira": 2500,
    "microondas": 350,
    "fogão": 1300,
    "liquidificador": 220
}

print("Lista sem desconto: ", lista_produtos)
nova_lista = {chave: valor*0.95 for chave, valor in lista_produtos.items()}
print("Lista com desconto: ", nova_lista)
