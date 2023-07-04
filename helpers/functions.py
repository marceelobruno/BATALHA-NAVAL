"""Este módulo contém todas as funções utilizadas no jogo Batalha Naval
desenvolvido para a disciplina Algoritmo e Programação Estruturada
pelos alunos: Luiz Fernando, Lucas Kaique e Marcelo Bruno.

Returns:
    Por conter todas as funções utilizadas na construção, salvamento e
    carragamento das partidas, temos funções que retornam dados do tipo
    lista de lista e os exibe para o usuário, bem como função como a
    de salvamento da partida que não há retorno.
"""

# Bibliotecas utilizadas
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

    # Exemplo de posição da matriz: [0][0], quando a linha e a coluna forem igual a 0.
    # Verifica se há o número 1 abaixo da posição do exemplo informado acima.
    if (i + 1) < 9 and matriz[i + 1][j] == 1:
        return False

    # Verifica se há o número 1 imediatamente ao lado direito
    # do exemplo informado acima.
    elif (j + 1) < 9 and matriz[i][j + 1] == 1:
        return False

    # Verifica se há o número 1 imediatamente acima da posição do exemplo informado.
    elif (i - 1) >= 1 and matriz[i - 1][j] == 1:
        return False

    # Verifica se há o número 1 imediatamente ao lado esquerdo do exemplo informado.
    elif (j - 1) >= 1 and matriz[i][j - 1] == 1:
        return False

    # Verifica se há o número 1 na mesma posição do exemplo informado.
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

    # Exemplo de posição da matriz: [0][0], quando a linha e a coluna forem igual a 0.
    # Verifica se há o número 1 na diagonal direita,
    # abaixo da posição do exemplo informado acima.
    if (i + 1) < 9 and (j + 1) < 9 and matriz[i + 1][j + 1] == 1:
        return False

    # Verifica se há o número 1 na diagonal esquerda,
    # abaixo da posição do exemplo informado.
    elif (i + 1) < 9 and (j - 1) >= 1 and matriz[i + 1][j - 1] == 1:
        return False

    # Verifica se há o número 1 na diagonal direita,
    # acima da posição do exemplo informado.
    elif (i - 1) >= 1 and (j + 1) < 9 and matriz[i - 1][j + 1] == 1:
        return False

    # Verifica se há o número 1 na diagonal esquerda,
    # acima da posição do exemplo informado.
    elif (i - 1) >= 1 and (j - 1) >= 1 and matriz[i - 1][j - 1] == 1:
        return False

    else:
        return True


def gerar_tabuleiro(num_navios: int) -> list[list]:
    """Esta função gera o tabuleiro do jogo como uma matriz de elementos
    1 e 0 e os transforma em `N` (navio) e `A` (água). Esta função utiliza
    outras funções criadas, como: `verifica_adj_L()` e `verifica_adj_D()`.

    Args:
        num_navios (int): Número de navios da partida.

    Returns:
        list[list]: Retorna o tabuleiro gerado com os elementos `A` e `N`.
    """

    # Gerando cada matriz utilizando list comprehension
    matriz = [[0 for i in range(9)] for i in range(9)]

    cont = 0
    while True:
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        if verifica_adj_L(matriz, x, y) and verifica_adj_D(matriz, x, y):
            matriz[x][y] = 1
            cont += 1
            if cont == num_navios:
                break

    # Vetor contendo as referências (A a H)
    referencias_lin_col = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    for i in range(9):
        for j in range(9):
            if i == 0:
                matriz[i][j] = referencias_lin_col[j]
            elif j == 0:
                matriz[i][j] = referencias_lin_col[i * 1]
            elif matriz[i][j] == 1:
                matriz[i][j] = "N"
            else:
                matriz[i][j] = "A"

    return matriz


def exibir_tabuleiro(jogador1: list[list], jogador2: list[list]) -> list[list]:
    """A função exibe as frotas como uma matriz em forma de tabuleiro para os usuários.
    Caso a exibição das frotas seja feita antes da partida iniciar, esta será encerrada.

    Args:
        jogador1 (list[list]): Contém a frota do jogador 1.
        jogador2 (list[list]): Contém a frota do jogador 2.

    Returns:
        list[list]: As frotas dos jogadores.
    """

    print("\nJogador 1")
    print()
    for i in range(9):
        for j in range(9):
            print(f"{jogador1[i][j]:4}", end=" ")
        print("")

    print("\nJogador 2")
    print()
    for i in range(9):
        for j in range(9):
            print(f"{jogador2[i][j]:4}", end=" ")
        print("")
    print()


def exibir_game(tab1: list[list], tab2: list[list]) -> list[list]:
    """A função recebe uma matriz existente com todos os seus índices preenchidos
    pela letra `X` e faz o tratamento adicionando para cada jogador um tabuleiro
    referenciado a primeira linha e coluna pelas letras (A a H).

    Args:
        tab1 (list[list]): Tabuleiro do jogador 1
        tab2 (list[list]): Tabuleiro do jogador 2

    Returns:
        list[list]: Os tabuleiros dos jogadores
    """

    # Vetor contendo as referências (A a H)
    referencias_lin_col = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    print("\nJogador 1")
    print()
    for i in range(9):
        for j in range(9):
            if i == 0:
                tab1[i][j] = referencias_lin_col[j]
            elif j == 0:
                tab1[i][j] = referencias_lin_col[i * 1]
            print(f"{tab1[i][j]:4}", end=" ")
        print("")

    print("\nJogador 2")
    print()
    for i in range(9):
        for j in range(9):
            if i == 0:
                tab2[i][j] = referencias_lin_col[j]
            elif j == 0:
                tab2[i][j] = referencias_lin_col[i * 1]
            print(f"{tab2[i][j]:4}", end=" ")
        print("")


def salva_jogo(jog1: list[list], jog2: list[list], folderPath: str,
               tab1: list[list], tab2: list[list], nome1: str, nome2: str,
               numNavios: int):
    """Salva a partida em andamento possibilitando uma posterior continuação.
    A função baseai-se nos nomes fornecidos pelos jogadores e deve obedecer a ordem:
    `nome do 1° jogador` + `nome do 2° jogador`, uma vez que o diretório é salvo
    da seguinte forma: `Player1_Player2`.

    Args:
        jog1 (list[list]): Matriz contendo a partida do jogador 1.
        jog2 (list[list]): Matriz contendo a partida do jogador 2.
        folderPath (str): Caminho onde o jogo será salvo.
        tab1 (list[list]): Matriz contendo o tabuleiro da partida do jogador 1.
        tab2 (list[list]): Matriz contendo o tabuleiro da partida do jogador 2.
        nome1 (str): Nome do jogador 1.
        nome2 (str): Nome do jogador 2.
        numNavios (int): Número de navios de cada jogador.

    """

    # Transforma o parâmetro folderPath em um caminho relativo.
    caminho = fr'boards/{folderPath}'

    # Cria o diretório caso o caminho informado não exista.
    if not os.path.exists(caminho):
        os.makedirs(caminho)

    # Se o diretório for criado na chamada da função ou já
    # existir, salvará a partida no caminho informado.
    if os.path.exists(caminho):

        # Salvando partida, tabuleiro e nome do jogador_1
        with open(fr'{caminho}/player_1.pkl', 'wb') as plyr_1:
            pickle.dump(jog1, plyr_1)

        with open(fr'{caminho}/tab_1.pkl', 'wb') as tb_1:
            pickle.dump(tab1, tb_1)

        with open(fr'{caminho}/player_1_name.txt', 'wb') as plyrN_1:
            pickle.dump(nome1, plyrN_1)

        # Salvando a quantidade de navios da partida
        with open(fr'{caminho}/navio.txt', 'wb') as navio:
            pickle.dump(numNavios, navio)

        # Salvando partida, tabuleiro e nome jogador_2
        with open(fr'{caminho}/player_2.pkl', 'wb') as plyr_2:
            pickle.dump(jog2, plyr_2)

        with open(fr'{caminho}/tab_2.pkl', 'wb') as tb_2:
            pickle.dump(tab2, tb_2)

        with open(fr'{caminho}/player_2_name.txt', 'wb') as plyrN_2:
            pickle.dump(nome2, plyrN_2)


def carrega_jogo(plyr_1: list[list], plyr_2: list[list],
                 folderPath: str, tb_1: list[list], tb_2: list[list],
                 nome1: str = "gen1", nome2: str = "gen2", numNavios: int = 1) -> list[list]:
    """Carregar uma partida existente e que foi armazenada na memória.
    A função baseai-se nos nomes fornecidos pelos jogadores e deve
    obedecer a ordem: `nome do 1° jogador` + `nome do 2° jogador`,
    uma vez que o diretório é salvo da seguinte forma: `\Player1_Player2\`,
    sendo os nomes dos jogadores separados por um `_`.

    Args:
        plyr_1 (list[list]): Matriz contendo a partida do jogador 1.
        plyr_2 (list[list]): Matriz contendo a partida do jogador 2.
        folderPath (str): Caminho onde o jogo será carregado.
        tb_1 (list[list]): Matriz contendo o tabuleiro da partida do jogador 1.
        tb_2 (list[list]): Matriz contendo o tabuleiro da partida do jogador 2.
        nome1 (str): Nome do jogador 1.
        nome2 (str): Nome do jogador 2.
        numNavios (int): Número de navios de cada jogador.
    """

    # Transforma o parâmetro folderPath em um caminho relativo.
    caminho = fr'boards/{folderPath}'

    # Verifica se o caminho informado para recupeação do jogo existe, caso
    # contrário, o usuário terá que informar novamente os nomes dos jogadores.
    if not os.path.exists(caminho):
        print('Partida desconhecida. Tente novamente!')

    else:
        # Carregando partida, tabuleiro e nome do jogador_1
        with open(fr'{caminho}/player_1.pkl', 'rb') as plyr_1:
            plyr_1 = pickle.load(plyr_1)

        with open(fr'{caminho}/tab_1.pkl', 'rb') as tb_1:
            tb_1 = pickle.load(tb_1)

        with open(fr'{caminho}/player_1_name.txt', 'rb') as nome1:
            nome1 = pickle.load(nome1)

        # Carregando a quantidade de navios da partida
        with open(fr'{caminho}/navio.txt', 'rb') as numNavios:
            numNavios = pickle.load(numNavios)

        # Carregando partida, tabuleiro e nome do jogador_2
        with open(fr'{caminho}/player_2.pkl', 'rb') as plyr_2:
            plyr_2 = pickle.load(plyr_2)

        with open(fr'{caminho}/tab_2.pkl', 'rb') as tb_2:
            tb_2 = pickle.load(tb_2)

        with open(fr'{caminho}/player_2_name.txt', 'rb') as nome2:
            nome2 = pickle.load(nome2)

        return plyr_1, plyr_2, tb_1, tb_2, nome1, nome2, numNavios


def coordenada(coord: str) -> int:
    """A função recebe um caractere e o transforma em um `int`.
    Caso o caractere informado esteja entre as letras (A a H)
    este será utilizado como coordenada na matriz. Caso seja `0`
    fará chamada ao menu. Por fim, se for qualquer outro caractere
    que não (0 ou A - H) será atribuído o valor de `9`.
    Args:
        coord (str): Um caractere representando a referência da linha/coluna.
    Returns:
        int: A função retorna uma posição no tabuleiro.
    """

    match coord:
        case '0':
            return 0
        case 'A':
            return 1
        case 'B':
            return 2
        case 'C':
            return 3
        case 'D':
            return 4
        case 'E':
            return 5
        case 'F':
            return 6
        case 'G':
            return 7
        case 'H':
            return 8
        case _:
            return 9


def game(jogador1: list[list], jogador2: list[list],
         tab_1: list[list], tab_2: list[list],
         nomeJogador_1: str, nomeJogador_2: str,
         numNavios: int):
    """Função principal que possibilita a jogabilidade
    da partida Batalha Naval.

    Args:
        jogador1 (list[list]): Frota do jogador 1.
        jogador2 (list[list]): Frota do jogador 2.
        tab_1 (list[list]): Tabuleiro do jogador 1.
        tab_2 (list[list]): Tabuleiro do jogador 2.
        nomeJogador_1 (str): Nome do jogador 1.
        nomeJogador_2 (str): Nome do jogador 2.
        numNavios (int): Número de navios da partida.
    """
    exibir_game(tab_1, tab_2)
    event = 0
    contAcertos_player1 = 0
    contAcertos_player2 = 0
    while True:
        while True:

            print("\nPara acessar o menu digite: 0")

            # Ações do Jogador 1
            print(f"\nVez do jogador 1 - {nomeJogador_1}")
            print()

            linha = coordenada(input("Digite a posição da linha (A - H): ").upper())

            if linha == 0:
                event = 1
                break

            coluna = coordenada(input("Digite a posição da coluna (A - H): ").upper())

            if linha < 9 and coluna < 9:
                if tab_2[linha][coluna] == "F":
                    print("Você já acertou essa posição perdeu a vez!!")
                    break
                if jogador2[linha][coluna] == "N":
                    tab_2[linha][coluna] = 'F'
                    contAcertos_player1 += 1

                    print()
                    with open('helpers/shot.txt', 'r', encoding='utf-8') as fogo:
                        print(fogo.read())

                    print(f"Você acertou!\nFaltam {numNavios-contAcertos_player1} navios.")
                    if contAcertos_player1 == numNavios:
                        print("\nParabéns!! Você ganhou!")
                        event = 1
                        break

                    exibir_game(tab_1, tab_2)
                else:
                    print()
                    with open('helpers/water.txt', 'r', encoding='utf-8') as agua:
                        print(agua.read())

                    tab_2[linha][coluna] = 'A'
                    exibir_game(tab_1, tab_2)
                    break

            else:
                print("\nPosição inválida")
                print("Perdeu a vez!")
                print()
                break

        if event == 1:
            break

        while True:

            print("\nPara acessar o menu digite: 0")

            # Ações do Jogador 2
            print(f"\nVez do jogador 2 - {nomeJogador_2}")
            print()

            linha = coordenada(input("Digite a posição da linha (A - H): ").upper())
            if linha == 0:
                event = 1
                break

            coluna = coordenada(input("Digite a posição da coluna (A - H): ").upper())

            if linha < 9 and coluna < 9:
                if tab_1[linha][coluna] == "F":
                    print("Você já acertou essa posição perdeu a vez!!")
                    break
                if jogador1[linha][coluna] == "N":
                    tab_1[linha][coluna] = 'F'
                    contAcertos_player2 += 1

                    print()
                    with open('helpers/shot.txt', 'r', encoding='utf-8') as fogo:
                        print(fogo.read())

                    print(f"Você acertou!\nFaltam {numNavios-contAcertos_player2} navios.")
                    if contAcertos_player2 == numNavios:
                        print("\nParabéns!! Você ganhou!")
                        event = 1
                        break

                    print()

                    exibir_game(tab_1, tab_2)
                    print()
                else:
                    print()
                    with open('helpers/water.txt', 'r', encoding='utf-8') as agua:
                        print(agua.read())

                    tab_1[linha][coluna] = 'A'
                    exibir_game(tab_1, tab_2)
                    print()
                    break
            else:
                print("\nPosição inválida")
                print("Perdeu a vez!")
                print()
                break

        if event == 1:
            break

    return jogador1, jogador2, tab_1, tab_2, nomeJogador_1, nomeJogador_2, event
