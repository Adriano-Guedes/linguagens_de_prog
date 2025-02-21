inicio = int(input("Informe o início do intervalo: "))
fim = int(input("Informe o fim do intervalo: "))
for i in range(inicio, fim + 1):
    if i % 2 != 0:
        print(i)
