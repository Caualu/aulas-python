data = int(input("diga o ano do nascimento:"))
anoAtual = int(input("digite o ano atual:"))
ano = anoAtual - 1
if data  < 2010 or anoAtual >= 2024:

 for anos in range (data,anoAtual-1):
   print(f"{data} voce tinha {anos} anos ")



