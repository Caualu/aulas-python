horas_atual = int(input("digite horaio atual(formato 24h, apenas a hora):"))
if horas_atual < 8 or horas_atual >= 18 :
    print("erro: fora do horario do expediente. o  sistema so funciona entre 8h ate 18h ")

else :
    
    for hora in range (horas_atual, 18 ):
        
        atividade = input (f"oque voce fez ou vai fazer as {hora}h?")
        





