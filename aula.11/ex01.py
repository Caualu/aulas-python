x =int(input("disque o seu numero e ache seu tesouro: "))
lista=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x =int(input("disque o seu numero e ache seu tesouro (voce tem 3 tentativas!): "))
while x != 3:
    print ("sem tesouro")
    x =int(input("disque o seu numero e ache seu tesouro (voce tem 2 tentativas!): "))
    if x != 3:
         x =int(input("disque o seu numero e ache seu tesouro (voce tem 1 tentativas!): "))
         print("numero de tentativas esgotadas.")
    break


while x == 3:
    print ("tesouro encontrado!")
    break