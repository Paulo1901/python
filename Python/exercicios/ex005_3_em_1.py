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
saudacao = input('Que horas são? ')

saudacao_int = int(saudacao)

if saudacao_int <= 11:
    print('Bom dia.')
elif saudacao_int >= 12 and saudacao_int <= 17:
    print('Boa tarde')
elif saudacao_int >= 18 and saudacao_int <= 23:
    print('Boa noite')
else:
    print('Por favor digite uma hora valida.')

"""
Faça um programa que peça o primeiro nome do usuário, se o nome tiver 4 letras ou menos
escreva "Seu nome é curto" se tiver 5 e 6 letras, esvreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é grande"
"""