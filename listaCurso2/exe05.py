frase = input("Informe as palavras separadas por expaço:")
palavras = frase.split()

listaOrdena = sorted(palavras)
print(f"Lista ordenada: {listaOrdena}")
quantidadePalavras = len(listaOrdena)
print(f"Quantidade de palavras: {quantidadePalavras}")

for p in listaOrdena:
    p.upper()
    print(f"{p.upper()}")

