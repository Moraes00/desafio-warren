numerodealunos = 3
tempoChegada = [-2 ,-1 , 0, 1, 2]
normal = []
atraso = []

for x in tempoChegada:
    if x <= 0:
        normal.append(1)
    elif x > 0:
        atraso.append(1)

if len(normal) >= numerodealunos:
    print("Aula Normal")
else:
    print("Aula Cancelada")