def contar_vogais(frase):
    vogais = 'aeiou'
    contagem = {vogal: 0 for vogal in vogais}

    for letra in frase.lower():
        if letra in contagem:
            contagem[letra] += 1

    return contagem

frase = input("Digite uma frase: ")

vogais_contadas = contar_vogais(frase)
print("Quantidade de vogais:")
for vogal, quantidade in vogais_contadas.items():
    print(f"{vogal}: {quantidade}")

print("Frase ao contrário:")
print(frase[::-1])

print("Frase sem espaços:")
print(frase.replace(' ', '-'))
