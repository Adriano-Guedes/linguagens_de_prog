def a():
    while True:
        try:
            num = int(input("Informe um número: "))
            print(f"Dobro = {num*2}")
            break
        except ValueError:
            print("Informe um número inteiro")

a()