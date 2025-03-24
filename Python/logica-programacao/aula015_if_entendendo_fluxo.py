# if /  elif      / else
# se / se não se / se não

"""
Na condição if só executada um bloco de cada vez,
apenas quando a condição for verdadeira.
"""
condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = False


if condicao1:
    print('Código para codição 1')
    # Podendo ter quantass linhas
    # forem necessarias
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita')

print('Fora do condição')
