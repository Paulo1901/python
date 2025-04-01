# Calculadora com while

while True:
    
    sair = input('Quer sair? [s]sim: ').lower().startswith('s')
    
    if sair is True:
        break