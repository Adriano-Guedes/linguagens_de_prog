horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))
valor_por_hora = float(input("Informe o valor recebido por hora: "))

salario = horas_trabalhadas * valor_por_hora

print(f"O salário total do mês é: R${salario:.2f}")
