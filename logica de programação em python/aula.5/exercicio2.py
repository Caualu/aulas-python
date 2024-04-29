categoria = int(input("digite o numero da categoria"))
distancia = float(input("a distancia q o cliente ira percorrer"))

catBlack = distancia * 2
catConfort = distancia * 1.5
catConvencional = distancia * 1
taxi = distancia * 3 
 
if categoria == 1: 
 print(f"voce adquiriu a categoria catBlack\n totalApagar {catBlack}") 
elif categoria == 2:
 print(f"voce adquiriu a categoria catConfort\n totalApagar {catConfort}")
elif categoria == 3: 
 print(f"voce adquiriu a categoria catConvencional\n totalApagar {catConvencional} ")
elif categoria == 4: 
 print(f"voce adquiriu a categoria taxi\n totalApagar {taxi}")

else:
 nomeCategoria = ("dados imvalidos") 
