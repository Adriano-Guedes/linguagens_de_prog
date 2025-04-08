def contar_pares(n):
    for i in range(1, n + 1):
        if i%2 == 0:
            yield i


num = int(input("informe um número: "))
retorno = contar_pares(num)

for x in retorno:
    print(x)