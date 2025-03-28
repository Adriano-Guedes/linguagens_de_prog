class SaldoInsuficienteException(Exception):
    def __init__(self, mensagem="Saldo insuficiente"):
        super().__init__(mensagem)

saldo = 1000

while True:
    try:
        print(f"Saldo atual: R$ {saldo:.2f}")
        saque = float(input("Informe o valor do saque: "))

        if saque <= 0:
            print("O valor do saque deve ser maior que zero.")
            continue
        
        if saque > saldo:
            raise SaldoInsuficienteException()
        
        saldo -= saque
        print(f"Saque realizado com sucesso! Saldo restante: R$ {saldo:.2f}")
        break
    
    except ValueError:
        print("Valor inválido. Por favor, insira um número válido.")
    except SaldoInsuficienteException as e:
        print(e)
