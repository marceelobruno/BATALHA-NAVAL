"""
Este módulo contém o arquivo principal do jogo Batalha Naval
desenvolvido para a disciplina Algoritmo e Programação Estruturadas
pelos alunos: Luiz Fernando, Lucas Kaique e Marcelo Bruno.
"""

from functions_APE import exibir_game, gerar_tabuleiro, menu


# Abre a logo inicial do jogo
with open('helpers/game_logo.txt', 'r', encoding='utf-8') as logo:
    print(logo.read())

while True:
    numeroNavios = int(input("Digite o número de navios (1 - 6): "))
    # if numeroNavios <= 6 and numeroNavios > 0:
    if 0 < numeroNavios <= 6:
        break
    print("Insira um valor válido entre 1 e 6!")

# Captura o nome dos jogadores
print('Informe os nomes dos jogadores:')
nomeJogador_1 = input('Jogador 1: ').title()
nomeJogador_2 = input('Jogador 2: ').title()

# Gera o path através dos nomes dos jogadores
folder_path = nomeJogador_1 + '_' + nomeJogador_2

jogador1 = gerar_tabuleiro(numeroNavios)
jogador2 = gerar_tabuleiro(numeroNavios)

tab_1 = [["X" for i in range(9)] for i in range(9)]
tab_2 = [["X" for i in range(9)] for i in range(9)]

test = menu(jogador1, jogador2, folder_path, tab_1, tab_2)
event = 0
while test:
    if test:

        tiro = 'N'
        while tiro == 'N':
            exibir_game(tab_1, tab_2)

            print("\nPara acessar o menu digite: 0")

            # Ações do Jogador 1
            print(f"\nVez do jogador 1 - {nomeJogador_1}")
            print()

            linha = int(input("Digite a posição da linha: "))
            coluna = int(input("Digite a posição da coluna: "))

            if linha == 0 or coluna == 0:
                e = menu(jogador1, jogador2, folder_path, tab_1, tab_2)
                if e is False:
                    event = 1
                break

            if linha < 9 and coluna < 9:
                if tab_1[linha][coluna] == "F":
                    tiro = 'A'
                    break
                if jogador1[linha][coluna] == "N":
                    tab_1[linha][coluna] = 'F'
                    print()
                    with open('helpers/shot.txt', 'r', encoding='utf-8') as fogo:
                        print(fogo.read())

                    exibir_game(tab_1, tab_2)
                else:
                    print()
                    with open('helpers/water.txt', 'r', encoding='utf-8') as agua:
                        print(agua.read())

                    tab_1[linha][coluna] = 'A'
                    exibir_game(tab_1, tab_2)
                    tiro = "A"

            else:
                print("Digite um valor válido.")
                print("\nPerdeu a vez!")
                print()

        if event == 1:
            break

        tiro = 'N'
        while tiro == 'N':
            print("\nPara acessar o menu digite: 0")

            # Ações do Jogador 2
            print(f"\nVez do jogador 2 - {nomeJogador_2}")
            print()

            linha = int(input("Digite a posição da linha: "))
            if linha == 0:
                e = menu(jogador1, jogador2, folder_path, tab_1, tab_2)
                if e is False:
                    event = 1
                break

            coluna = int(input("Digite a posição da coluna: "))

            if linha < 9 and coluna < 9:
                if tab_1[linha][coluna] == "F":
                    tiro = 'A'
                    break
                if jogador1[linha][coluna] == "N":

                    tab_2[linha][coluna] = 'F'
                    print()
                    with open('helpers/shot.txt', 'r', encoding='utf-8') as fogo:
                        print(fogo.read())

                    exibir_game(tab_1, tab_2)
                    print()
                else:
                    print()
                    with open('helpers/water.txt', 'r', encoding='utf-8') as agua:
                        print(agua.read())

                    tab_2[linha][coluna] = 'A'
                    exibir_game(tab_1, tab_2)
                    tiro = 'A'
                    print()
            else:
                print("Digite um valor válido.")
                print("\nPerdeu a vez!")
                print()
        if event == 1:
            break
    else:
        print("Você encerrou o programa!!")
