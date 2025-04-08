from contador import Contador

num = int(input("Informe um número:"))

contador = Contador(num)

for numero in contador:
    print(numero)
