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

while True:
    letrada_digitada = input('Digite uma letra: ')

    # condição criada para digitar apenas uma letra
    if len(letrada_digitada) > 1:
        print('Digite apenas uma letra: ')
        continue
    
