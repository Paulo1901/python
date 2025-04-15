"""
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeados tem nome com sinal de igual
Argumentos não nomeados recebe apenas o argumento (valor)
"""

# Parametro é utilizando na definiçao da função
# arguamento é o valor que será atribuido as parametros

# Definindo a função
def soma(x, y, z):
    print(f'{x=} {y=} {z=}', '|', 'x + y + z =',x + y + z)

# Executandoa função
soma(1, 2, 5) # argumento posicional
soma(2, 1, z=3) # argumentos nomeados
