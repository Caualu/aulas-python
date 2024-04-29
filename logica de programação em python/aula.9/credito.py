from util import dobro 
 

# entrada do usuario 
limite_atual = float(input("digite o limite atual do seu controle de credito: R$"))


#calculadora o novo limite 
novo_limite = dobro (limite_atual) 


# imprine os resultados 
print(f"seu limite atual é {limite_atual}. seu novo limite seria R${novo_limite:.2f}.")