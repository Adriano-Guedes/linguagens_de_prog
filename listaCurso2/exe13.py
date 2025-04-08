try:
    with open("dados.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        quantidade = len(linhas)

        print(f"Quantidade de linhas: {quantidade}\n")
        print("Conteúdo do arquivo:")
        for linha in linhas:
            print(linha.strip())

except FileNotFoundError:
    print("Arquivo 'dados.txt' não encontrado.")