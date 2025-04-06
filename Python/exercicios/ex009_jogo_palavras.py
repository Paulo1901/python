"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
-Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra
-Qual o usuário digite uma letra, você
vai conferir se a letra digitada está
em palavra secreta.
    -Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    -Se a letra digitada nãoe stiver
    na palavra secreta; exbiba *.
Faça a contagem de tentativas do seu usuário
"""

# Palavra que usuário precisda adivinhar '???'
palavra_secreta = 'perfume'

# Essa variavel irá armzenar as letras que o usuário aceta
letras_acertadas = ''

while True:
    letra_digitada = input('Digite uma letra: ')

    # condição criada para digitar apenas uma letra
    if len(letra_digitada) > 1: 
        print('Digite apenas uma letra: ')
        continue
    
    # Verifica se letra_digitada está na palavra_secreta
    if letra_digitada in palavra_secreta:
        # atribuia a variavel letra_acertadas cada letra que o usuario acertar
        letras_acertadas += letra_digitada
    

    # essa variável é responsavel pela formatação da saído do programa
    palavra_formada = ''
    
    # Cria a lógica de verificar cada letra acerteza pelo usuário
    for letra_secreta in palavra_secreta: # iterando na variavel
        if letra_secreta in letras_acertadas: # checando o valor
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print(palavra_formada)
