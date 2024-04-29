data = int(input("diga o ano do nascimento:"))
anoAtual = int(input("digite o ano atual:"))
idade = anoAtual - data

    
for nascimento in range (data,anoAtual + 1):
   idade = nascimento - data
   print(f"{nascimento} voce tinha {idade} anos ")



