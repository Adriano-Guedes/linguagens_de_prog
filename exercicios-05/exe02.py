def primo(num):
    num = num
    num1 = num
    flag = 0
    while num > 0:
        if num1%num == 0:
            flag = flag+1
        if flag > 2:
            return False
        num = num-1
    return True
    

num = int(input("Informe um número: "))
print(f"O número {num} é primo?: {'SIM' if primo(num) else 'NÃO'}")
