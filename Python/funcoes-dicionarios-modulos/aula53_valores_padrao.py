"""
Valores padrões para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão, caso o valor não seja
enviado para o parametro, o valor padrão será
usado
"""

# IS NOT = checa se o valor de é de terminado tipo ou não 

def soma(x, y, z=0):
    if z is not None:
        print(f'{x=} {y=} {z=} =', x + y + z)
    else:
        print(f'{x=} {y=} =', x + y)


soma(1, 2)
soma(2, 2)
soma(100, 200)
soma(7, 9)
