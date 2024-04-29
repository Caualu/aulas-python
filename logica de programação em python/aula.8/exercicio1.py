soma=0
continuar = True # variavel de controle para loop

while continuar :
  
  print("digite 1 caso queira somar algum numero")
  print("digite 2 caso queira ver o seu somatario ") 
  print("digite 3 caso quiera encerra sessao")    
  opcao = input("escolha uma opcao (1, 2 ou 3):") #receba a opção do usuario


  if opcao == "1": 
    numero = input("digite o numero para poder somar") 
    soma += float(numero)
    print(f"numero{numero} adicionado a soma.") 
  elif opcao == "2":    
    print(f"somatorio atual: {soma} ")
  elif opcao == "3":
    break # altere a variavel de controle false para saor do loop 
  else:
    print("opcao invalida. por  favor, escolha 1, 2 ou 3.") # mensagem invalida 
 
 
    print (" programa encerrado. Somatorio final:", soma) # exibe a soma final quando o loop termina     