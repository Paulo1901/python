# if /  elif      / else
# se / se não se / se não

"""
fluxo de condicional
if, elif e else
servem para decidir o fluxo do programa,
"se ele não fizer isso faça aquilo", controlando assim o fluxo e decisões
do seu código, executando somente apena um bloco.
"""

entrada = input('Você quer entrar ou sair? ')

if entrada == 'entrar':
    print('Você entrou no sistema.')
    
    print(123456)
elif entrada == 'sair':
    print('Você saiu do sistema.')
else:
    print('Você não digitou nem entrar nem sair.')

print('fora dos blocos!')
