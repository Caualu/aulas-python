import time 
cafeteira = int(input("compre seu cafe0/n - expresso\n1 - tradicional\n2 - cappuccino\n3 - latte\n4 - descafeinado\n5")) 

opcao = input("escolha uma opcao (1, 2 , 3 , 4 , 5):") 
while True:
    if opcao == 1: 
      for expresso in range (1,11):
         print(f"seu cafe vai ficar pronto em 10 seg {expresso}")
      print("seu cafe esta pronto.")
      cafeteira = int(input("compre seu cafe0\n - expresso\n2 - tradicional\n3 - cappuccino\n4 - latte\n5 - descafeinado\n5")) 

    elif opcao == 2:   
       for tradicional2 in range (1,16):
         print(f"seu cafe vai ficar pronto em 15 seg {tradicional2}")
    print("seu cafe esta pronto")
    cafeteira = int(input("compre seu cafe -  expresso\n1 - tradicional\n2 - cappuccino\n3 - latte\n4 - descafeinado\n5")) 

      
    if opcao == 3:
         for cappuccino in range (1,23):
          print(f"seu cafe vai ficar pronto em 22 seg {cappuccino}")
    print("seu cafe esta pronto")  
    cafeteira = int(input("compre seu cafe0\n - expresso\n2 - tradicional\n3 - cappuccino\n4 - latte\n5 - descafeinado\n5")) 
       
       
        
    if opcao == 4:
         for latte in range (1,19):
          print(f"seu cafe vai ficar pronto em 22 seg {latte}")
    print("seu cafe esta pronto")  
    cafeteira = int(input("compre seu cafe0\n - expresso\n2 - tradicional\n3 - cappuccino\n4 - latte\n5 - descafeinado\n5")) 
       
    if opcao == 5:
         for descafeinado in range (1,21):
          print(f"seu cafe vai ficar pronto em 22 seg {latte}")
    print("seu cafe esta pronto")  
    cafeteira = int(input("compre seu cafe0\n - expresso\n2 - tradicional\n3 - cappuccino\n4 - latte\n5 - descafeinado\n5")) 


    print(f"Preparando seu {latte}... Por favor, aguarde.")
    for i in range(tempo, 0, -1):
      print(f"{i} segundos restantes...")
      time.sleep(1)
       
           