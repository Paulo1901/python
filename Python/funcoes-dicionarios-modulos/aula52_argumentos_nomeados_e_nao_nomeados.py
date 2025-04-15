"""
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeados tem nome com sinal de igual
Argumentos não nomeados recebe apenas o argumento (valor)
"""

# Definindo a função
def soma(x, y):
    print(f'{x=} {y=}', '|', 'x + y =',x + y)

# Executandoa função
soma(2, 1) # argumento posicional
soma(y=2, x=1) # argumentos nomeados
