dicionario = {
    "casa": "house",
    "carro": "car",
    "gato": "cat",
    "livro": "book",
    "feliz": "happy"
}
flag = False
palavra = input("Digite uma palavra: ")

for x, y in dicionario.items():
    if x == palavra:
        flag = True
        print(y)
if flag == False:
    print("Tradução não encontrada")