# solicite dois numeros ao usuario
# e compare qual o maior valor e exiba na tela

primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor:')

if primeiro_valor >= segundo_valor:
    print(f'{primeiro_valor} é maior ou igual ao {segundo_valor}')
else:
    print(f'O {segundo_valor} é maior que {primeiro_valor}')