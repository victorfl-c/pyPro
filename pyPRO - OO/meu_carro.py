from carro import Carro

carro_novo = Carro('Supra', 2002)

print(carro_novo.get_descricao())
carro_novo.set_odometro(345)
print(carro_novo.get_kilometragem())