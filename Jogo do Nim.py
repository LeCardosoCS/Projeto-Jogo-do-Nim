def computador_escolhe_jogada(n, m):
    M = m + 1
    R = n % M
    if R == 1:
      print("O computador tirou uma peça.")
    else:
      print("O computador tirou", R, "peças.")
    return R


def usuario_escolhe_jogada(n, m):
    J = int(input('\nQuantas peças você vai tirar? '))
    while J > m:
        J = int(input('Oops! Jogada inválida! Tente de novo.\nQuantas peças você vai tirar? '))
    if J == 1:
        print("Você tirou uma peça.")
    else:
        print("Você tirou", J,"peças.")
    return J


def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    if n % (m + 1) == 0:
        print('\nVocê começa!')
        n = n - usuario_escolhe_jogada(n, m)
        if n > 1:
            print('Agora restam', n,'peças no tabuleiro.\n')
        elif n == 1:
            print(f'Agora resta apenas uma peça no tabuleiro.\n')
        while True:
            n = n - computador_escolhe_jogada(n, m)
            if n > 1:
                print('Agora restam', n,'peças no tabuleiro.')
            elif n == 1:
                print(f'Agora resta apenas uma peça no tabuleiro.')
            elif n == 0:
                break
            n = n - usuario_escolhe_jogada(n, m)
            if n > 1:
                print('Agora restam', n,'peças no tabuleiro.')
            elif n == 1:
                print('Agora resta apenas uma peça no tabuleiro.\n')
    else:
        print('\nComputador começa!\n')
        n = n - computador_escolhe_jogada(n, m)
        if n > 1:
            print('Agora restam', n,'peças no tabuleiro.')
        elif n == 1:
            print(f'Agora resta apenas uma peça no tabuleiro.')
        if n != 0:
            while True:
                n = n - usuario_escolhe_jogada(n, m)
                if n > 1:
                    print('Agora restam', n,'peças no tabuleiro.\n')
                elif n == 1:
                    print('Agora resta apenas uma peça no tabuleiro.\n')
                n = n - computador_escolhe_jogada(n, m)
                if n > 1:
                    print('Agora restam', n,'peças no tabuleiro.')
                elif n == 1:
                    print('Agora resta apenas uma peça no tabuleiro.')
                elif n == 0:
                    break

    print('Fim do jogo! O computador ganhou!')


def campeonato():

    print('\n**** Rodada 1 ****\n')
    partida()
    print("\n**** Rodada 2 ****\n")
    partida()
    print("\n**** Rodada 3 ****\n")
    partida()
    print("\n**** Final do campeonato! ****\n")
    print("Placar: Você", 0, "X", 3, "Computador")


print('\nBem-vindo ao jogo do NIM! Escolha:\n')
e = int(input('1 - para jogar uma partida isolada \n2 - para jogar um campeonato ' ))
if e == 1:
    print('\nVocê escolheu uma partida!\n')
    partida()
else:
    print('\nVocê escolheu um campeonato!\n')
    campeonato()
