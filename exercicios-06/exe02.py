num1 = int(input("Informe o número 1: "))
num2 = int(input("Informe o número 2: "))
num3 = int(input("Informe o número 3: "))
num4 = int(input("Informe o número 4: "))

tupla = (num1, num2, num3, num4)

qtd9 = tupla.count(9)
index3 = tupla.index(3)
pares = [num for num in tupla if num % 2 == 0]

print(f"Quantidade de 9s: {qtd9}\nPosição do primeiro 3: {index3}\nNúmeros pares: {pares}")