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


def verifica_adj_L(matriz: list[list], i: int, j: int) -> bool:
    """Esta função verifica se há valores 1 acima, abaixo, à esquerda
    ou à direita de um outro valor 1 selecionado na matriz.

    Args:
        matriz (list[list]): Refere-se à matriz gerada.
        i (int): Refere-se à linha da matriz.
        j (int): Refere-se à coluna da matriz.

    Returns:
        Bool: Retorna True se não houver nenhum valor 1 adjacente pelos
        lados. Retorna False caso o contrário ou se a posição matriz[i][j]
        já estiver ocupada por um valor 1.
    """

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


def verifica_adj_D(matriz: list[list], i: int, j: int) -> bool:
    """Esta função verifica se há valores 1 nas diagonais de um
    outro valor 1 selecionado na matriz.


    Args:
        matriz (list[list]): Refere-se à matriz gerada.
        i (int): Refere-se à linha da matriz.
        j (int): Refere-se à coluna da matriz.

    Returns:
        Bool: Retorna True se não houver nenhum valor 1 adjacente
        pelas diagonais. Caso contrário, retornará False.
    """

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


def gerar_tabuleiro(num_navios):
    """Esta função gera o tabuleiro do jogo como uma matriz de elementos
    1 e 0 e os transforma em "N" e "A". Esta função utiliza outras funções
    criadas, como: verifica_adj_L() e verifica_adj_D().

    Args:
        num_navios (int):  contém o número de navios selecionados.

    Returns:
        Retorna o tabuleiro gerado com os elementos "A" (água) e "N" (navio)
    """

    matriz = [[0 for i in range(8)] for i in range(8)]
    cont = 0
    while True:
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        if verifica_adj_L(matriz, x, y) and verifica_adj_D(matriz, x, y):
            matriz[x][y] = 1
            cont += 1
            if cont == num_navios:
                break

    for i in range(8):
        for j in range(8):
            if matriz[i][j] == 1:
                matriz[i][j] = "N"
            else:
                matriz[i][j] = "A"

    return matriz


def exibir_tabuleiro(jogador1: list[list], jogador2: list[list]) -> list[list]:
    """A função exibe as frotas como uma matriz em forma de tabuleiro para os usuários. 
    Caso a exibição das frotas seja feita antes da partida iniciar, esta será encerrada.

    Args:
        jogador1 (list[list]):Contém a frota do jogador 1.
        jogador2 (list[list]): Contém a frota do jogador 2.

    Returns:
        list[list]: As frotas dos jogadores.
    """

    print("\nJogador 1")
    print()
    for i in range(8):
        for j in range(8):
            print(f"{jogador1[i][j]:4}", end="")
        print("")

    print("\nJogador 2")
    print()
    for i in range(8):
        for j in range(8):
            print(f"{jogador2[i][j]:4}", end="")
        print("")
    print()


def exibir_game(tab1: list[list], tab2: list[list]) -> list[list]:
    """Exibe para cada jogador um tabuleiro com as casas em forma de `X`.

    Args:
        tab1 (list[list]): Tabuleiro do jogador 1
        tab2 (list[list]): Tabuleiro do jogador 2

    Returns:
        list[list]: Os tabuleiros dos jogadores
    """

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


def salva_jogo(jog1: list[list], jog2: list[list], folderPath: str, tab1, tab2):
    """Salva a partida em andamento possibilitando uma posterior continuação.
    A função baseai-se nos nomes fornecidos pelos jogadores e deve obedecer a ordem:
    `nome do 1° jogador` + `nome do 2° jogador`, uma vez que o diretório é salvo
    da seguinte forma: `Player1_Player2`.

    Args:
        jog1 (list): Matriz contendo a partida do jogador 1
        jog2 (list): Matriz contendo a partida do jogador 2
        folderPath (str): Caminho onde o jogo será salvo
    """

    # Transforma o parâmetro folderPath em um caminho relativo.
    caminho = fr'boards/{folderPath}'

    # Cria o diretório caso o path informado não exista.
    if not os.path.exists(caminho):
        os.makedirs(caminho)

    # Se o diretório for criado na chamada da função ou já existir,
    # salvará a partida no caminho informado.
    if os.path.exists(caminho):
        with open(fr'{caminho}/player_1.pkl', 'wb') as output:
            pickle.dump(jog1, output)

        with open(fr'{caminho}/player_2.pkl', 'wb') as output:
            pickle.dump(jog2, output)


def carrega_jogo(jog1: list[list], jog2: list[list], folderPath: str, tab1, tab2) -> list[list]:
    """Carrega uma partida existente e que foi armazenada na memória.
    A função baseai-se nos nomes fornecidos pelo jogador e deve obedecer a ordem:
    `nome do 1° jogador` + `nome do 2° jogador`, uma vez que o diretório é salvo
    da seguinte forma: `Player1_Player2`.

    Args:
        jog1 (list): Matriz contendo a partida do jogador 1.
        jog2 (list): Matriz contendo a partida do jogador 2.
        folderPath (str): Caminho onde o jogo será carregado.
    """

    # Transforma o parâmetro folderPath em um caminho relativo.
    caminho = fr'boards/{folderPath}'

    # Verificando se o caminho informado para recupeação do jogo existe, caso
    # contrário, o usuário terá que informar novamente os nomes dos jogadores.
    if not os.path.exists(caminho):
        print('Partida desconhecida. Tente novamente!')

    else:
        # Carregando partida do jogador_1
        with open(fr'{caminho}/player_1.pkl', 'rb') as player_1_file:
            jog1 = pickle.load(player_1_file)

        # Exibe a partida do jogador_1
        for i in range(len(jog1)):
            for j in range(len(jog1)):
                print(f'{jog1[i][j]:4}', end=" ")
            print()

        print()

        # Carregando partida do jogador_2
        with open(fr'{caminho}/player_2.pkl', 'rb') as player_2_file:
            jog2 = pickle.load(player_2_file)

        # Exibe a partida do jogador_2
        for i in range(len(jog2)):
            for j in range(len(jog2)):
                print(f'{jog2[i][j]:4}', end=" ")
            print()


def menu(jog1: list[list], jog2: list[list], folder_path: str) -> str:
    """ Apresenta comandos básicos de um menu que podem ser selecionados
    ao digitar um número inteiro. Esta função utiliza-se de outras funções,
    como: `carrega_jogo()`,`exibir_tabuleiro()` e `salva_jogo()`.

    Args:
        jog1 (list): Matriz contendo a partida do jogador 1.
        jog2 (list): Matriz contendo a partida do jogador 2.
        folderPath (str): Caminho onde o jogo será carregado.
    """

    print("""\

Menu:
    Digite 1 para iniciar um novo jogo:
    Digite 2 para carregar um jogo:
    Digite 3 para exibir as frotas:
    Digite 4 para sair do jogo:
    """)

    menu = int(input("Digite o que deseja: "))

    if menu == 1:
        return True
    elif menu == 2:
        carrega_jogo(jog1, jog2, folder_path, tab1, tab2)
    elif menu == 3:
        exibir_tabuleiro(jog1, jog2)
    elif menu == 4:
        salvar = input(('\nDeseja salvar o jogo (S/N)?: ')).upper()
        if salvar == 'S':
            salva_jogo(jog1, jog2, folder_path, tab1, tab2)
            print('Partida salva!')
            return False
        elif salvar == 'N':
            print("Você encerrou o programa sem salvar!")
            return False
    else:
        return False

