"""
Faça um lista de compras com listas
o usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
nao permita que o programa quebre com
erro de indices inexistentes na lista
"""
import os

lista = [] # criando uma lista vazia
while True:
    # interação com usuário
    print('Selecione uma opção')
    opcao = input('[i]inserir [a]apagar [l]lista ')

    if opcao == 'i':
        os.system('cls') # limpando terminal
        valor = input('Valor: ') # solicitando ao usuario o valor
        lista.append(valor) # atrinbuindo um valor a lista
    elif opcao == 'a':
        print('a')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')
        
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor escolha i, a ou l')
