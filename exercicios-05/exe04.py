def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    contador = sum(1 for letra in palavra if letra in vogais)
    return contador

palavra = input("Digite uma palavra: ")
quantidade_vogais = contar_vogais(palavra)
print(f"A palavra '{palavra}' tem {quantidade_vogais} vogal(is).")