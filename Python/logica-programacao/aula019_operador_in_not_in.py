# Operadores in e not in
# Strings são iteraveis
# 0 1 2 3 4
# P a u l o
#-4-3-2-1-0

# nome = 'Paulo'
# print(nome[1])
# print(nome[-4])

# print('a' in nome) # condição
# print('z' in nome)
# print(10 * '-')
# print('a' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que você gostaria de encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em nome.')
else:
    print(f'{encontrar} não esta em {nome}')

