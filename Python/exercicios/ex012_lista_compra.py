"""
Faça um lista de compras com listas
o usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
nao permita que o programa quebre com
erro de indices inexistentes na lista
"""
lista = [] # criando uma lista vazia
while True:
    # interação com usuário
    print('Selecione uma opção')
    opcao = input('[i]inserir [a]apagar [l]lista ')

    if opcao == 'i':
        print('i')
    elif opcao == 'a':
        print('a')
    elif opcao == 'l':
        print('l')
    else:
        print('Por favor escolha i, a ou l')
