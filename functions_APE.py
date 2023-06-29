"""Este módulo contém todas as funções utilizadas no jogo Batalha Naval.

Returns:
    Por conter todas as funções utilizadas na construção, salvamento e
    carragamento das partidas, temos funções que retornam dados do tipo
    lista de lista e os exibe para o usuário, bem como função como a
    de salvamento da partida que não há retorno.
"""

import os
import pickle
import random


# Verifica se as celulas laterais a posição (i, j) está disponível.
def verifica_adj_L(matriz, i, j):
    if (i + 1) < 8 and matriz[i + 1][j] == 1:
        return False
    elif (j + 1) < 8 and matriz[i][j + 1] == 1:
        return False
    elif (i - 1) >= 0 and matriz[i - 1][j] == 1:
        return False
    elif (j - 1) >= 0 and matriz[i][j - 1] == 1:
        return False
    elif matriz[i][j] == 1:
        return False
    else:
        return True


# Verifica se as celulas diagonais na posição (i, j) está disponível.
def verifica_adj_D(matriz, i, j):
    if (i + 1) < 8 and (j + 1) < 8 and matriz[i + 1][j + 1] == 1:
        return False
    elif (i + 1) < 8 and (j - 1) >= 0 and matriz[i + 1][j - 1] == 1:
        return False
    elif (i - 1) >= 0 and (j + 1) < 8 and matriz[i - 1][j + 1] == 1:
        return False
    elif (i - 1) >= 0 and (j - 1) >= 0 and matriz[i - 1][j - 1] == 1:
        return False
    else:
        return True


# Gera o tabuleiro
def gerar_tabuleiro(N):
    matriz = [[0 for i in range(8)] for i in range(8)]
    cont = 0
    while True:
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        if verifica_adj_L(matriz, x, y) and verifica_adj_D(matriz, x, y):
            matriz[x][y] = 1
            cont += 1
            if cont == N:
                break

    for i in range(8):
        for j in range(8):
            if matriz[i][j] == 1:
                matriz[i][j] = "N"
            else:
                matriz[i][j] = "A"

    return matriz


# Exibe as frotas
def exibir_tabuleiro(jogador1, jogador2):
    print()
    print("Jogador 1")
    print()
    for i in range(8):
        for j in range(8):
            print(f"{jogador1[i][j]:4}", end="")
        print("")

    print()
    print("Jogador 2")
    print()

    for i in range(8):
        for j in range(8):
            print(f"{jogador2[i][j]:4}", end="")
        print("")
    print()


# Exibe o tabuleiro para o jogo.
def exibir_game(tab1, tab2):
    print("\nJogador 1")
    print()

    for i in range(8):
        for j in range(8):
            print(f"{tab1[i][j]:4}", end="")
        print("")

    print("\nJogador 2")
    print()

    for i in range(8):
        for j in range(8):
            print(f"{tab2[i][j]:4}", end="")
        print("")
    print()


def salva_jogo(jog1: list[list], jog2: list[list], folderPath: str):
    """Salva a partida em andamento possibilitando uma posterior continuação.
    A função baseai-se nos nomes fornecidos pelos jogadores e deve obedecer a ordem:
    `nome do 1° jogador` + `nome do 2° jogador`, uma vez que o diretório é salvo
    da seguinte forma: `Player1_Player2`.

    Args:
        jog1 (list): Matriz contendo a partida do jogador 1
        jog2 (list): Matriz contendo a partida do jogador 2
        folderPath (str): Caminho onde o jogo será salvo
    """

    # Transforma o parâmetro folderPath em um caminho relativo
    caminho = fr'boards\{folderPath}'

    # Cria o diretório caso o path informado não exista
    if not os.path.exists(caminho):
        os.makedirs(caminho)

    # Se o diretório informado for criado na chamada da função ou já existir,
    # salvará a partida no path.
    if os.path.exists(caminho):
        with open(fr'{caminho}\player_1.pkl', 'wb') as output:
            pickle.dump(jog1, output)

        with open(fr'{caminho}\player_2.pkl', 'wb') as output:
            pickle.dump(jog2, output)


def carrega_jogo(jog1: list[list], jog2: list[list], folderPath: str) -> list[list]:
    """Carrega uma partida existente e que foi armazenada na memória.
    A função baseai-se nos nomes fornecidos pelo jogador e deve obedecer a ordem:
    `nome do 1° jogador` + `nome do 2° jogador`, uma vez que o diretório é salvo
    da seguinte forma: `Player1_Player2`.

    Args:
        jog1 (list): Matriz contendo a partida do jogador 1.
        jog2 (list): Matriz contendo a partida do jogador 2.
        folderPath (str): Caminho onde o jogo será carregado.
    """

    # Transforma o parâmetro folderPath em um caminho relativo
    caminho = fr'boards\{folderPath}'

    # Verificando se o caminho informado para recupeação do jogo existe,
    # caso contrário, o usuário terá que informar novamente os nomes dos jogadores
    if not os.path.exists(caminho):
        print('Partida desconhecida. Tente novamente!')

    else:
        # Carregando partida jogador_1
        with open(fr'{caminho}\player_1.pkl', 'rb') as player_1_file:
            jog1 = pickle.load(player_1_file)

        # Exibe a partida jogador_1
        for i in range(len(jog1)):
            for j in range(len(jog1)):
                print(f'{jog1[i][j]:4}', end=" ")
            print()

        print()

        # Carregando partida jogador_2
        with open(fr'{caminho}\player_2.pkl', 'rb') as player_2_file:
            jog2 = pickle.load(player_2_file)

        # Exibe a partida jogador_2
        for i in range(len(jog2)):
            for j in range(len(jog2)):
                print(f'{jog2[i][j]:4}', end=" ")
            print()


# Gera o menu interativo
def menu(jog1, jog2, folder_path: str):
    print("""\

Menu:
    Digite 1 para iniciar um novo jogo:
    Digite 2 para exibir as frotas:
    Digite 3 para sair do jogo:
    Digite 4 para carregar um jogo:
    """)

    menu = int(input("Digite o que deseja: "))

    if menu == 1:
        return True
    elif menu == 2:
        exibir_tabuleiro(jog1, jog2)
    elif menu == 3:
        salvar = input(('\nDeseja salvar o jogo (S/N)?: ')).upper()
        if salvar == 'S':
            salva_jogo(jog1, jog2, folder_path)
            print('Partida salva!')
        elif salvar == 'N':
            print("Você encerrou o programa sem salvar!")
    elif menu == 4:
        carrega_jogo(jog1, jog2, folder_path)
    else:
        return False
