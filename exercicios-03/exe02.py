soma = 0
while True:
    numero = float(input("Informe um número (ou um negativo para encerrar): "))
    if numero < 0:
        break
    soma += numero
print(f"A soma de todos os números positivos é: {soma}")
