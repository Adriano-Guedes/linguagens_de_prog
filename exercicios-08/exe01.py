try:
    num1 = int(input("Informe um número:"))
    num2 = int(input("Informe outro número:"))

    result = num1 / num2

    print(f"Resultado: {result}")
except ValueError:
    print("Informe apensa números inteiros")
except ZeroDivisionError:
    print("Valores tem que ser maior que zero ")