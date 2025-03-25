# Operadores lógicos 
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser 
# verdeiras.
# Se qualquer valor for considerando falso,
# expressão inteira será avaliada naquele valor 
# são considerados falsy (que você ja viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]entrar [S]sair: ')
senha_digitada = input('Senha: ')

senha_permituda = '123456'
# 'and' as duas condições precisa ser verdadeira
if entrada == 'E' and senha_digitada == senha_permituda:
    print('Usuário entrou no sistema.')
else:
    print('Usuário saiu do sistema.')

