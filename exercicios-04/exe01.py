lista = []
numeros = input("Informe uma listagem de números separando por ',': ")
total = 0

lista = [int(num) for num in numeros.split(",")]
for x in lista:
    total = total + x

print(total)
