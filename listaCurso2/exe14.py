import struct

numeros = [10, 20, 30, 40, 50]

with open("dados.bin", "wb") as arquivo:
    for numero in numeros:
        arquivo.write(struct.pack("i", numero))

numeros_lidos = []
with open("dados.bin", "rb") as arquivo:
    while True:
        dados = arquivo.read(4)
        if not dados:
            break
        numero = struct.unpack("i", dados)[0]
        numeros_lidos.append(numero)

print("Números lidos do arquivo binário:")
print(numeros_lidos)