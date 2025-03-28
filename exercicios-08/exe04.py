lista = [1,2,3,4,5]
while True:
    try:
        num = int(input("Informe um número: "))
        print(f"Valor {lista[num]} no índice {num}")
        break
    except IndexError:
        print("Valor de índice fora do range da lista")