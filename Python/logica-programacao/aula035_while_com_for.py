"""
'for' é utilizado quando sabemos onde desejamo chega
quantas iterações serão enecessarias

'while' Ja o while é ustilizando quando não sabemos
a condição de parada do código
"""

for i in range(10):
    if i == 2:
        print('i é 2, pulando')
        continue

    if i == 8:
        print('i é 8, seu else não executa')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('fora completo com sucesso!')
