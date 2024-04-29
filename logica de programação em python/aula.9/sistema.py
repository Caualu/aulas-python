from multi import soma, subtração, multiplicaçao, divisao


while True:
   opcao = int(input("digite 1 para somar dois numeros\nDigite 2 para subtrair dois numeros\nDigite 3 para multiplicar dois numeros \nDigite 4 para dividir dois numeros \nDigite 5 para encerrar o programa:"))
   if opcao == 1: 
    num1 = int(input("digite o 1° numero"))
    num2 = int(input("digite o 2° numero"))
    soma1 = soma (num1,num2)
    print(f"o resultado da soma {soma1}.") 
   elif opcao == 2:
    num1 = int(input("digite o 1° numero"))
    num2 = int(input("digite o 2° numero"))
    subtração1 = subtração (num1,num2)
    print(f"o resultado da subtração {subtração1}.")   
   elif opcao == 3:
    num1 = int(input("digite o 1° numero"))
    num2 = int(input("digite o 2° numero"))
    multiplicação1 = multiplicaçao (num1,num2)
    print(f"o resultado da multiplicação {multiplicação1}.")      
   elif opcao == 4:
    num1 = int(input("digite o 1° numero"))
    num2 = int(input("digite o 2° numero"))
    divisao1 = divisao (num1,num2)
    print(f"o resultado da divisao {divisao1}.")  
   elif opcao == 5:
     break















