try:
    nomeArquivo = input("Informe o nome do arquivo: ")

    f = open(f"{nomeArquivo}.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("Arquivo não encontrado")
except FileExistsError:
    print("Arquivo não encontrado")