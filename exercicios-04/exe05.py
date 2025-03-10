numeros = input("Informe uma listagem de números separando por ',': ")
num = int(input("Informe um número: "))
qtdNum = 0

lista = [int(n) for n in numeros.split(",")]

qtdNum = lista.count(num)

print(f"Quantidade de repetições de '{num}': {qtdNum}")
