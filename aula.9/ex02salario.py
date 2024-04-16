salario = float(input("diga seu salario:"))

multiplicaçao = salario *1

print(f"seu decimo terceiro salario será {multiplicaçao}")

from util import dobro 
valor_emprestado = float(input("digite o valor que deseja emprestar: R$"))

total_pagar = dobro (valor_emprestado)

print (f"valor emprestado: R${valor_emprestado:.2f}.total a pagar após um ano: R${total_pagar:.2f}.")
