"""
Este módulo contém o arquivo principal do jogo Batalha Naval
desenvolvido para a disciplina Algoritmo e Programação Estruturadas
pelos alunos: Luiz Fernando, Lucas Kaique e Marcelo Bruno.
"""

from functions_APE import *

# Abre a logo inicial do jogo
with open('helpers/game_logo.txt', 'r', encoding='utf-8') as logo:
    print(logo.read())

print("Antes de começar:")
cont = 0
while True:
    numeroNavios = int(input("Digite o número de navios (1 - 6): "))
    if 0 < numeroNavios <= 6:
        break
    print("Insira um valor válido entre 1 e 6!")

jogador1 = gerar_tabuleiro(numeroNavios)
jogador2 = gerar_tabuleiro(numeroNavios)
tab_1 = tab_2 = [["X" for i in range(9)] for i in range(9)]

while True:
    
    print("""\

Menu:
    Digite 1 para iniciar um novo jogo:
    Digite 2 para carregar um jogo:
    Digite 3 para exibir as frotas:
    Digite 4 para sair e salvar:
    Digite 5 para sair sem salvar
    """)

    menu = int(input("Digite o que deseja: "))

    if menu == 1:
        # Captura o nome dos jogadores
        jogador1 = gerar_tabuleiro(numeroNavios)
        jogador2 = gerar_tabuleiro(numeroNavios)
        print('Informe os nomes dos jogadores: ')
        nomeJogador_1 = input('Jogador 1: ').title()
        nomeJogador_2 = input('Jogador 2: ').title()

        cont = 1

        tab_1 = [["X" for i in range(9)] for i in range(9)]
        tab_2 = [["X" for i in range(9)] for i in range(9)]

        jogador1, jogador2, tab_1, tab_2, nomeJogador_1, nomeJogador_2 = game(jogador1, jogador2, tab_1, tab_2, nomeJogador_1, nomeJogador_2)
        
    elif menu == 2:
        folder_path = input("informe o nome da partida que deseja carregar: ").lower()

        cont = 1

        jogador1, jogador2, tab_1, tab_2, nomeJogador_1, nomeJogador_2 = carrega_jogo(jogador1, jogador2, folder_path, tab_1, tab_2)

        game(jogador1, jogador2, tab_1, tab_2, nomeJogador_1, nomeJogador_2)

    elif menu == 3:
        exibir_game(jogador1, jogador2)
    elif menu == 4:
        if cont == 0:
            nomeJogador_1 = input('Jogador 1: ').title()
            nomeJogador_2 = input('Jogador 2: ').title()

            folder_path = input("informe o nome da partida que deseja carregar: ").lower()

            salva_jogo(jogador1, jogador2, folder_path, tab_1, tab_2, nomeJogador_1, nomeJogador_2)
            print('Partida salva!')
            break
        else:
            folder_path = input("informe o nome da partida que deseja carregar: ").lower()
            salva_jogo(jogador1, jogador2, folder_path, tab_1, tab_2, nomeJogador_1, nomeJogador_2)
            print('Partida salva!')
            break
        
    else:
        print("Você encerrou o programa sem salvar!")
        break

