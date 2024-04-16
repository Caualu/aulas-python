from util import dobro 

salario_mensal = float(input("digite o seu salario mensal: R$"))

valor_recebido = dobro(salario_mensal)

print(f"seu salario mensal é R${salario_mensal:.2f}. voce receberá R${valor_recebido:.2f} camo o 13° salario.")
