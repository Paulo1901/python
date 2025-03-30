"""
Faça um programa que peça ao usuario para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro
"""
numero = input('Digite um número: ')

if numero.isdigit():
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print(f'O {numero_int} é par.')
    else:
        print(f'O {numero_int} é impar.')
else:
    print('Você não digitou um número.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horario
descrito, exiba a saudação apropriada ex:
Bom dia 0-11, boa tarde 12-17 e boa noite 18-23
"""
entrada_hora = input('Que horas são? ')

entrada_hora_int = int(entrada_hora)

if entrada_hora_int >= 0 and entrada_hora_int <= 11:
    print('Bom dia.')
elif entrada_hora_int >= 12 and entrada_hora_int <= 17:
    print('Boa tarde')
elif entrada_hora_int >= 18 and entrada_hora_int <= 23:
    print('Boa noite')
else:
    print('Por favor digite uma hora valida.')

"""
Faça um programa que peça o primeiro nome do usuário, se o nome tiver 4 letras ou menos
escreva "Seu nome é curto" se tiver 5 e 6 letras, esvreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é grande"
"""

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto.')     
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal.')
    else:
        print('Seu nome é grande.')
else:
    print('Digite mais de uma letra.')