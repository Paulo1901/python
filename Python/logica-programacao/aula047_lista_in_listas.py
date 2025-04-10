# Lista de demtro de lista

salas = [
#     0        1     
    ['Paulo', 'Andreia', ], # 0
#     0     
    ['Fabiana'], # 1
#     0       1       2
    ['Luiz', 'João', 'Eduardo'] # 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][2])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
