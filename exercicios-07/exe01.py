dicionario = {}

while len(dicionario) < 3:
    nome = input("Informe o nome: ")
    nota = float(input("Informe a nota: "))
    dicionario[nome] = nota

for x,y in dicionario.items():
    print(f"Nome: {x}\nNota: {y}")
    print("----------")
