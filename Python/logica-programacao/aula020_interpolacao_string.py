# Interpolação basica de string
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF0123456789)

nome = 'Paulo'
preco = 1000.95897643
variavel = '%s, o preco é R$%.2f' % (nome, preco)
print(variavel)
# Transformando em Hexadecimal
print('O Hexadecimal de %d é %08x' % (1500, 1500))
