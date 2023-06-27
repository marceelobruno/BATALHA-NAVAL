import random

#verifica se as celulas laterais a posição (i, j) está disponível.
def verifica_adj_L(matriz, i, j):
        if (i+1) < 8 and matriz[i+1][j] == 1:
            return False
        elif (j+1) < 8 and matriz[i][j+1] == 1:
            return False
        elif (i-1) >= 0 and matriz[i-1][j] == 1:
            return False
        elif (j-1) >= 0 and matriz[i][j-1] == 1:
            return False
        elif matriz[i][j] == 1:
            return False
        else: 
            return True

#verifica se as celulas diagonais a posição (i, j) está disponível.
def verifica_adj_D(matriz, i, j):
        if (i+1) < 8 and (j+1) < 8 and matriz[i+1][j+1] == 1:
            return False
        elif (i+1) < 8 and (j-1) >= 0 and matriz[i+1][j-1] == 1:
            return False
        elif (i-1) >= 0 and (j+1) < 8 and matriz[i-1][j+1] == 1:
            return False
        elif (i-1) >= 0 and (j-1) >= 0 and matriz[i-1][j-1] == 1:
            return False
        else: 
            return True

#gera o tabuleiro
def gerar_tabuleiro(N):
    matriz = [[0 for i in range(8)] for i in range(8)]
    cont = 0
    while True:
        x = random.randint(0,7)
        y = random.randint(0,7)
        if verifica_adj_L(matriz, x, y) and verifica_adj_D(matriz, x, y):
            matriz[x][y] = 1
            cont +=1 
            if cont == N:
                break

    for i in range(8):
        for j in range(8):
            if matriz[i][j] == 1:
                matriz[i][j] = "N"
            else:
                matriz[i][j] = "A"

    return matriz

#exibe as frotas 
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

#exibe o tabuleiro para o jogo.
def exibir_game(tab1, tab2):
    print()
    print("Jogador 1")
    print()

    for i in range(8):
        for j in range(8):
            print(f"{tab1[i][j]:4}", end="")
        print("")

    print()
    print("Jogador 2")
    print()

    for i in range(8):
        for j in range(8):
            print(f"{tab2[i][j]:4}", end="")
        print("")
    print()

#gera o menu interativo
def menu(jog1, jog2):
    print("""\
    
    Bem vindo a BATALHA NAVAL:

    Menu:
    Digite 1 para iniciar o Jogo:
    Digite 2 para exibir as frotas:
    Digite 3 para encerrar o Jogo:

    """)
        
    menu = int(input("Digite o que deseja: "))
    if menu == 1:
        return True
    elif menu == 2:
       exibir_tabuleiro(jog1, jog2)
    else:
        return False
    