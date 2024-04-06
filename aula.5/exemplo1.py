vendas = int(input("digite o número de vendas: "))

# Condicional para deerminar o nível 
if vendas <= 50:
 nivel = 1
elif vendas <= 100:
 nivel = 2
elif vendas <= 150:
 nivel = 3
elif vendas <= 200:
  nivel = 4 
else:
  nivel = 5 

 # exibindo o resulado 
print(f"com {vendas} vendas, você está no nivel {nivel} de desempenho.")  
 
  
             