#loja de tapete 
categoria = int(input("digite qual tapete o cliente vai consumir"))
metro = float(input("qunatos metros de tapete"))
 
tapeteConvencional = metro * 10 
tapetePremiun = metro * 20
tapeteMaxPremiun = metro * 30 

if categoria == 1:
    print(f"voce adquiriu o tapeteConvencional\n totalApagar {tapeteConvencional}") 
elif categoria == 2: 
    print(f"voce adquiriu o tapetePremiun\n totalApagar{tapetePremiun}")
elif categoria == 3:
    print(f"voce adquiriu o tapeteMaxPremiun\n totalApagar {tapeteMaxPremiun}")
else:
    print("dados invalidos")











































