"""
Formatação basica de strings
s - string
d - int
f - float
<numeros de digitos>f
x - ou X Hexadecimais
(caractere)(><^)(quantidade)
esquerda
direita
centro
Sinais + ou -
= - Força o numero aperecer antes do zero
EX: 0>100,1f
conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # direita 
print(f'{variavel: <10}.') # esquerda
print(f'{variavel: ^10}.') # centro
print(f'{125.4547787445455:+.2f}')
print(f'{125.4547787445455:0=+10.2f}')
