tupla = ("Flamengo", "Palmeiras", "São Paulo", "Grêmio", "Cruzeiro", "Vasco", "Atlético Mineiro", "Internacional", "Santos", "Corinthians")

print(f"Primeiro: {tupla[0]}")
print(f"Segundo: {tupla[1]}")
print(f"Terceiro: {tupla[2]}")
print("-----------------")
print(f"Décimo: {tupla[9]}")
print(f"Nono: {tupla[8]}")
print(f"Oitavo: {tupla[7]}")

ordenado = tuple(sorted(tupla))

nome = input("Informe um time:")

if nome in tupla:
    indice = tupla.index(nome)
    print(f"O time {nome} está na posição {indice + 1} da tupla.")
else:
    print(f"O time {nome} não foi encontrado na tupla.")