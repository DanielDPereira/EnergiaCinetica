import numbers

print("Bem vindo a calculadora de energia cinética")

print("Obs: para usar números decimais, use . no lugar de , ")

m = float(input("Defina a massa (em kg): "))
v = float(input("Defina a velocidade (em m/s): "))

Ec = (m*v ** 2)/2

print("A energia cinética é "+str(Ec)+"J")

#Para fechar
input("Digite <ENTER> para fechar o programa")