lista = []
numeros = input("Informe uma listagem de números separando por ',': ")
maior = 0
menor = 0

lista = [int(num) for num in numeros.split(",")]
menor = lista[0]
for x in lista:
    if x > maior:
        maior = x
    if x < menor:
        menor = x

print(f"Maior: {maior}")
print(f"Menor: {menor}")
