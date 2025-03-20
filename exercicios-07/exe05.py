dicionario = {
    1: "caneta",
    2: "papel",
    3: "lapiz",
    4: "borracha",
    5: "apagador"
}
cod = int(input("Digite o código: "))

for x, y in dicionario.items():
    if x == cod:
        print(y)
