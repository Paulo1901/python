"""
Calculo do primeiro digito do CPF
CPF: 746.824.890-70
Coleta a soma dos 9 primeiros do CPF
multiplicando cada um dos valores por uma 
contagem regressiva começando com 10

EX:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
   7   4  6  8  2  4  4  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultador: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9
    resultado = 0
contrario disso:
    resultado é o valor da conta

o primeiro digito do CPF é 7
"""
cpf = '74682489070'
nove_digito = cpf[:9] # pegando os numeros primeiros digitos do cpf

# criando um contador regressivo
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digito:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1 
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)
