sta_atletas = []
numero_atletas = 1
print("Por favor, insira a distância dos lançamentos:")
for i in range(10):
    distancia = float(input(f"O atleta {i + 1} fez o lançamento a qual distância?: "))
    numero_atletas.append(distancia)

for distanciaporatleta in numero_atletas:
    print(f"O atleta {numero_atletas} lançou a uma distancia de {distanciaporatleta} metros")
    numero_atletas += 1

numero_atletas.sort()
numero_atletas.reverse()
print("Lançamentos ordenados:", numero_atletas)