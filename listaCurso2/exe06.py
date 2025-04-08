num1 = float(input("Informe um número: "))
num2 = float(input("Informe outro número: "))

try:
    print(f"{num1} / {num2}: {num1/num2}")
except ZeroDivisionError:
    print("Divisão por 0 não pemitida")
except ValueError:
    print("Valores incorretos")