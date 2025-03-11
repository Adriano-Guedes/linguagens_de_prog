def mediaLista(lista = []):
    qtd = 0
    total = 0
    for x in lista:
        total += x
        qtd += 1
    return total/qtd

lista = []
numeros = input("Informe uma listagem de números separando por ',': ")

lista = [int(num) for num in numeros.split(",")]

print(f"Media da lista: {mediaLista(lista)}")