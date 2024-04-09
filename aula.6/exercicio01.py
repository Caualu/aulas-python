cartao =(input(" voce possui cartao black? (sim/nao):")).lower()
salaVip = input("voce tem ingresso da sala vip? (sim/nao):").lower()
#lower: pra nao bugar o sistema com a letra maiuscula 
if cartao == "sim" or salaVip == "sim": 
    print("voce tem acesso a sala vip")

else:
    print("voce nao tem acesso a sala vip")    
