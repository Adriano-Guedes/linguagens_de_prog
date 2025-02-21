n = int(input("Informe o número N para exibir os N primeiros termos da sequência de Fibonacci: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
