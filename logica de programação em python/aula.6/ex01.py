idade = int(input("digite sua idade:"))
assinante = input("voce é assinante do game pass? (sim/não):").lower()

if idade > 18 and assinante == "sim":
    print("voce tem acesso ao game pass!")
else: 
    print("voce nã0 tem acesso ao game pass.")

