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

    # Verifica se há o número 1 imediatamente ao lado direito do exemplo informado acima.
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
    # Verifica se há o número 1 na diagonal direita, abaixo da posição do exemplo informado acima.
    if (i + 1) < 9 and (j + 1) < 9 and matriz[i + 1][j + 1] == 1:
        return False

    # Verifica se há o número 1 na diagonal esquerda, abaixo da posição do exemplo informado.
    elif (i + 1) < 9 and (j - 1) >= 1 and matriz[i + 1][j - 1] == 1:
        return False

    # Verifica se há o número 1 na diagonal direita, acima da posição do exemplo informado.
    elif (i - 1) >= 1 and (j + 1) < 9 and matriz[i - 1][j + 1] == 1:
        return False

    # Verifica se há o número 1 na diagonal esquerda, acima da posição do exemplo informado.
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
    """A função recebe uma matriz existente com todos os seus índices preenchidos pela
    letra `X` e faz o tratamento adicionando para cada jogador um tabuleiro referenciado
    a primeira linha e coluna pelas letras (A a H).

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
               tab1: list[list], tab2: list[list]):
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
    """

    # Transforma o parâmetro folderPath em um caminho relativo.
    caminho = fr'boards/{folderPath}'

    # Cria o diretório caso o caminho informado não exista.
    if not os.path.exists(caminho):
        os.makedirs(caminho)

    # Se o diretório for criado na chamada da função ou já
    # existir, salvará a partida no caminho informado.
    if os.path.exists(caminho):

        # Salvando partida e o tabuleiro do jogador_1
        with open(fr'{caminho}/player_1.pkl', 'wb') as plyr_1:
            pickle.dump(jog1, plyr_1)

        with open(fr'{caminho}/tab_1.pkl', 'wb') as tb_1:
            pickle.dump(tab1, tb_1)

        # Salvando partida e o tabuleiro do jogador_2
        with open(fr'{caminho}/player_2.pkl', 'wb') as plyr_2:
            pickle.dump(jog2, plyr_2)

        with open(fr'{caminho}/tab_2.pkl', 'wb') as tb_2:
            pickle.dump(tab2, tb_2)


def carrega_jogo(plyr_1: list[list], plyr_2: list[list], folderPath: str,
                 tb_1: list[list], tb_2: list[list], nome1: str = "Player_1", nome2: str = "Player_2" ) -> list[list] :
    """Carrega uma partida existente e que foi armazenada na memória.
    A função baseai-se nos nomes fornecidos pelos jogadores e deve
    obedecer a ordem: `nome do 1° jogador` + `nome do 2° jogador`, uma vez
    que o diretório é salvo da seguinte forma: `\Player1_Player2\`, sendo os
    nomes dos jogadores separados por um `_`.

    Args:
        plyr_1 (list[list]): Matriz contendo a partida do jogador 1.
        plyr_2 (list[list]): Matriz contendo a partida do jogador 2.
        folderPath (str): Caminho onde o jogo será carregado.
        tb_1 (list[list]): Matriz contendo o tabuleiro da partida do jogador 1.
        tb_2 (list[list]): Matriz contendo o tabuleiro da partida do jogador 2.
    """

    # Transforma o parâmetro folderPath em um caminho relativo.
    caminho = fr'boards/{folderPath}'

    # Verifica se o caminho informado para recupeação do jogo existe, caso
    # contrário, o usuário terá que informar novamente os nomes dos jogadores.
    if not os.path.exists(caminho):
        print('Partida desconhecida. Tente novamente!')

    else:
        # Carregando partida e o tabuleiro do jogador_1
        with open(fr'{caminho}/player_1.pkl', 'rb') as plyr_1:
            plyr_1 = pickle.load(plyr_1)

        with open(fr'{caminho}/tab_1.pkl', 'rb') as tb_1:
            tb_1 = pickle.load(tb_1)

        # Carregando partida e o tabuleiro do jogador_2
        with open(fr'{caminho}/player_2.pkl', 'rb') as plyr_2:
            plyr_2 = pickle.load(plyr_2)

        with open(fr'{caminho}/tab_2.pkl', 'rb') as tb_2:
            tb_2 = pickle.load(tb_2)

        return game(plyr_1, plyr_2, tb_1, tb_2, nome1, nome2)


def menu(jog1=None, jog2=None, tab1=None, tab2=None) -> str:
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
    Digite 4 para sair e salvar:
    Digite 5 para sair sem salvar
    """)

    

    menu = int(input("Digite o que deseja: "))

    if menu == 1:
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

        jogador1 = gerar_tabuleiro(numeroNavios)
        jogador2 = gerar_tabuleiro(numeroNavios)

        tab_1 = [["X" for i in range(9)] for i in range(9)]
        tab_2 = [["X" for i in range(9)] for i in range(9)]

        game(jogador1, jogador2, tab_1, tab_2, nomeJogador_1, nomeJogador_2)

    elif menu == 2:
        folder_path = input("informe o nome da partida que deseja carregar").lower()
        carrega_jogo(jog1, jog2, folder_path, tab1, tab2)

    elif menu == 3:
        exibir_game(jogador1, jogador2)

    elif menu == 4:
        folder_path = input("Infome o nome dessa partida").lower()
        salva_jogo(jog1, jog2, folder_path, tab1, tab2)
        print('Partida salva!')
        return False
    else:
        print("Você encerrou o programa sem salvar!")
        return False

def game(jogador1, jogador2, tab_1, tab_2, nomeJogador_1, nomeJogador_2):
    exibir_game(tab_1, tab_2)
    event = 0
    while True:
        while True:
            print("\nPara acessar o menu digite: 0")

            # Ações do Jogador 1
            print(f"\nVez do jogador 1 - {nomeJogador_1}")
            print()

            linha = int(input("Digite a posição da linha: "))
            coluna = int(input("Digite a posição da coluna: "))

            if linha == 0 or coluna == 0:
                e = menu()
                if e is False:
                    event = 1
                break

            if linha < 9 and coluna < 9:
                if tab_1[linha][coluna] == "F":
                    print("Você já acertou essa posição perdeu a vez !!")
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
                    break

            else:
                print("Posição inválida")
                print("\nPerdeu a vez!")
                print()
                break

        if event == 1:
            break

        while True:
            print("\nPara acessar o menu digite: 0")

            # Ações do Jogador 2
            print(f"\nVez do jogador 2 - {nomeJogador_2}")
            print()

            linha = int(input("Digite a posição da linha: "))
            if linha == 0:
                e = menu(jogador1, jogador2, tab_1, tab_2)
                if e is False:
                    event = 1
                break

            coluna = int(input("Digite a posição da coluna: "))

            if linha < 9 and coluna < 9:
                if tab_2[linha][coluna] == "F":
                    print("Você já acertou essa posição perdeu a vez !!")
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
                    print()
                    break
            else:
                print("Posição inválida")
                print("\nPerdeu a vez!")
                print()
                break

        if event == 1:
            break
