"""
Introdução ao try/execept
Try -> tantar executar o código
execept -> ocorreu algum erro ao tenatr executar
"""

numero_str = input('Vou dobrar o numero que você digitar: ')

# fail fast, erra o mais rapiudo possivel para mandar para capitura
try:
    print('STR', numero_str)
    numero_float = float(numero_str) # convertendo a str para float
    print('FLOAT', numero_float)
    print(f'O dobro do {numero_str} que você difgitou é {numero_float * 2:.2f}')
except:
    print('Isso não é um número.')

# print(numero_str.isdigit()) 
# if numero_str.isdigit():
#     numero_float = float(numero_str) # convertendo a str para float
#     print(f'O dobro do {numero_str} que você difgitou é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número.')