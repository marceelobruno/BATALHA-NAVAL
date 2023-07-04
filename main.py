"""
Este módulo contém o arquivo principal do jogo Batalha Naval
desenvolvido para a disciplina Algoritmo e Programação Estruturadas
pelos alunos: Luiz Fernando, Lucas Kaique e Marcelo Bruno.
"""

# Importando as funções
from helpers.functions import *

# Abre a logo inicial do jogo
with open('helpers/game_logo.txt', 'r', encoding='utf-8') as logo:
    print(logo.read())

# Solicitando a quantidade de navios de cada tabuleiro
print("\nAntes de começar:")
cont = 0
while True:
    numeroNavios = int(input("Digite o número de navios (1 - 6): "))
    if 0 < numeroNavios <= 6:
        break
    print("Insira um valor válido entre 1 e 6!")

# Gerando os tabuleiros dos jogadores com base
# na quantidade de navios informados.
jogador1 = gerar_tabuleiro(numeroNavios)
jogador2 = gerar_tabuleiro(numeroNavios)

# Mascarando os tabuleiros com a letra 'X
tab_1 = tab_2 = [["X" for i in range(9)] for i in range(9)]

while True:

    print("""\n
Menu:
    Digite 1 para iniciar um novo jogo:
    Digite 2 para carregar um jogo:
    Digite 3 para exibir as frotas:
    Digite 4 para sair e salvar:
    Digite 5 para sair sem salvar:
    """)

    menu = int(input("Digite o que deseja: "))

    # Iniciando uma nova partida
    if menu == 1:

        jogador1 = gerar_tabuleiro(numeroNavios)
        jogador2 = gerar_tabuleiro(numeroNavios)

        # Captura o nome dos jogadores
        print('\nInforme os nomes dos jogadores:')
        nomeJogador_1 = input('Jogador 1: ').title()
        nomeJogador_2 = input('Jogador 2: ').title()

        cont = 1

        # Gerando os tabuleiros usando list comprehension
        tab_1 = [["X" for i in range(9)] for i in range(9)]
        tab_2 = [["X" for i in range(9)] for i in range(9)]

        game(jogador1,jogador2, tab_1, tab_2,nomeJogador_1, nomeJogador_2,numeroNavios)

    # Carregando um jogo existente
    elif menu == 2:
        folder_path = input("Informe o nome da partida que deseja carregar: ").lower()

        cont = 1

        jogador1, jogador2, tab_1, tab_2, nomeJogador_1, nomeJogador_2,numeroNavios = carrega_jogo(jogador1,
                                                                                      jogador2,
                                                                                      folder_path,
                                                                                      tab_1, tab_2,numeroNavios)

        game(jogador1, jogador2, tab_1, tab_2, nomeJogador_1, nomeJogador_2,numeroNavios)

    # Exibindo as frotas dos jogadores.
    # Esta opção se ativada encerrará a partida.
    elif menu == 3:
        exibir_game(jogador1, jogador2)

    # Opção para sair do jogo e salvá-lo
    elif menu == 4:
        if cont == 0:
            nomeJogador_1 = input('Jogador 1: ').title()
            nomeJogador_2 = input('Jogador 2: ').title()

            folder_path = input("Informe o nome da partida que deseja salvar: ").lower()

            salva_jogo(jogador1, jogador2, folder_path,
                       tab_1, tab_2, nomeJogador_1, nomeJogador_2,numeroNavios)
            print('Partida salva!')
            break

        else:
            folder_path = input("Informe o nome da partida que deseja salvar: ").lower()
            salva_jogo(jogador1, jogador2, folder_path,
                       tab_1, tab_2, nomeJogador_1, nomeJogador_2,numeroNavios)
            print('Partida salva!')
            break

    # Opção que encerra o jogo sem salvá-lo
    elif menu == 5:
        print("Você encerrou a partida sem salvar!")
        break
    # Caso o usuário informe uma opção não existente no menu
    else:
        print("Opção não encontrada. O programa encerrou!")
        break
