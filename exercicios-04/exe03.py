numeros = input("Informe uma listagem de números separando por ',': ")
lista = [int(num) for num in numeros.split(",")]

mylist = list(dict.fromkeys(lista))
print(mylist)