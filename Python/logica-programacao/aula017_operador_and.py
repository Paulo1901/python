# Operadores lógicos 
# and (e) or (ou) not (não)
# or - Qual quer condição verdadeira avalia
# toda expressão como verdadeira.
# Se qualquer valor for considerando verdadeiro,
# expressão inteira será avaliada naquele valor 
# são considerados falsy (que você ja viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# entrada = input('[E]entrar [S]sair: ')
# senha_digitada = input('Senha: ')

# senha_permituda = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permituda:
#     print('Usuário entrou no sistema.')
# else:
#     print('Usuário saiu do sistema.')

# Avaliação de curto circuito

senha = input('Senha: ') or 'Sen senha'
print(senha)
