# Operador lógico 'not'
# Usado para inverter expressões
# not True = False
# not False = True


print(not 0) # False
print(not 1) # True

senha = input('Senha: ')

senha_para_entrar = '1234'

if not senha:
    print('Você não digitou nada.')
elif senha == senha_para_entrar:
    print('Você entrou')
