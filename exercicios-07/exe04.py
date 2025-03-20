frase = input("Digite uma frase: ")

palavras = frase.split()

contagem_palavras = {}

for palavra in palavras:
    palavra = palavra.lower()
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

print("\nFrequência das palavras na frase:")
print(contagem_palavras)
