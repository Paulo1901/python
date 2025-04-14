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
import re
import sys

# cpf_enviado_usuario = '392.321.168-63'\
#     .replace('.','')\
#     .replace('-','')\
#     .replace(' ','')

# expressão regular para tratar a string
entrada = input('CPF [746.824.890-70]: ')
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
    )

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados repetidos.')
    sys.exit()

nove_digito = cpf_enviado_usuario[:9] # pegando os numeros primeiros digitos do cpf
# criando um contador regressivo
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digito:
    resultado_digito_1 += int(digito) * contador_regressivo_1 
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digito + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2) * 10 % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digito}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido.')
else:
    print('CPF inválido')
