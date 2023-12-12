from random import randrange
def jogar():

    text_abertura()

    enforca = acertou = False
    erros = 0

    arquivo = open('palavras.txt', 'r')
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    p = randrange(0, len(palavras))
    palavra_secreta = palavras[p].upper()
    letras_acertadas = ['_' for _ in palavra_secreta]
    print(letras_acertadas, '\n')

    while not enforca and not acertou:
        chute = input('Diga uma letra: ').strip().upper()
        index = 0
        if chute in palavra_secreta:
            for letras in palavra_secreta:
                if chute == letras.upper():
                    letras_acertadas[index] = letras
                index += 1
            print(f'Sim temos a letra {chute} na palavra!')

        else:
            erros += 1
            print(f'Ops, você errou! Foram {erros} tentativas.')
            desenha_forca(erros)
            enforca = erros == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print('Parabéns!!! Você acertou todas as letras!!'
              f'\nA palavra secreta é {palavra_secreta}!!')
        mensagem_vencedor()
    else:
        print('Suas chances acabaram, infelizmente você perdeu!')
        mensagem_perdedor(palavra_secreta)
        print('Fim de Jogo')

def text_abertura():
    print('   ***********************************************')
    print('      \*/ Bem Vindo ao nosso Jogo de Forca! \*/')
    print('   ***********************************************')
    print('  Tente adivinhar a palavra que eu tenho escondida ;)'
          '\n                Você têm 7 chances!\n')

def mensagem_vencedor():
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if  erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def mensagem_perdedor(palavra_secreta):
    print("Você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("     _______________      ")
    print("    /               \     ")
    print("   /                 \    ")
    print("/\/                   \/\ ")
    print("\ |   XXXX     XXXX   | / ")
    print(" \|   XXXX     XXXX   |/  ")
    print("  |   XXX       XXX   |   ")
    print("  |                   |   ")
    print("  \__      XXX      __/   ")
    print("    |\     XXX     /|     ")
    print("    | |           | |     ")
    print("    | I I I I I I I |     ")
    print("    |  I I I I I I  |     ")
    print("    \_             _/     ")
    print("      \_         _/       ")
    print("        \_______/         ")

if __name__ == '__main__':
    jogar()