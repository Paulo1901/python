"""
Exercício 
Peça ao usuário para digitar seu nome
peça ao usuário para digitar sua idade
se nome e idade forem digitados
    Exiba:
        Seu nome é {nome}
        seu nome invertido é {nome invertido}
        se nome contém (ou não) espaços
        seu nome tem {n} letras
        a primeira letra do seu nome é {letra}
        a utiltima letra do seu nome é {letra}
se nada for digitado em nome ou idade:
    exiba: "Desculpe, você deixou campos vazios"
"""

nome = input('Digite seu nome: ').strip() # strip remove os espaços
idade = input('Digite sua idade: ')

if nome and idade: # condição que avalia se foi deixados campos vazios
    print(f'Seu nome é {nome}')
    print(f'Meu {nome} invertido é {nome[::-1]}') # nome invertido
    if ' ' in nome:
        print(f'Meu nome contem espaços')
    else:
        print('Não contem espaços')
    print(f'Meu {nome} tem {len(nome)} letras')
    print(f'A primeiro do meu nome é {nome[0]}')
    print(f'A ultima letra do meu nome é {nome[-1]}')
else:
    print('"Desculpe, você deixou campos vazios"')
    