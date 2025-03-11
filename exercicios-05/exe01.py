def fatorial(num):
    num = num
    atual = num-1
    while atual > 0:
        num = num*atual
        atual = atual-1
    return num

num = int(input("Digite um número inteiro: "))
print(f"Fatorial de {num}: {fatorial(num)}")
