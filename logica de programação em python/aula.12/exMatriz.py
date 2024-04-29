#crie uma matriz 9x9 representando um armario escolar vazio, onde cada iniciante contem 'vazio'
armario = [["vazio"] * 9 for linha in range (9)]
while True : 
    # solicita ao usuario as coordenadas e o item 
    linha = int(input("digite a linha (0-8):"))
    coluna = int(input("digite a coluna (0-8): ")) 
    item = (input("digite o nome do item a ser colocado:"))
    if 0 <= linha < 9 and  0 <= coluna < 9: 
        # coloca o item no slot correspondente 
        armario[linha][coluna]= item
        print (f"item '{item}' adicionado a posição ({linha} , {coluna}).")
    else:
        print("coordenadas invalidas! Por favor , digite valores entre 0 e 8 para linha e coluna.")
    #pergunta se o usuario deseja continuar  
    continuar = input ("deseja continuar outro item? (s/n):")
    if continuar.lower() != 's':
       remover = input("deseja retirar o item? (s/n)")
       linha = int(input("digite a linha (0-8):"))
       coluna = int(input("digite a coluna (0-8): ")) 
       armario = [["vazio"] * 9 for linha in range (9)]
       print (f"item '{item}' foi removido da posição ({linha} , {coluna}).")
    elif remover.lower() != 's':
       break

    #mostra o estado final do armario 
print("estado final do armario ")
for linha in armario:
         print(linha)


