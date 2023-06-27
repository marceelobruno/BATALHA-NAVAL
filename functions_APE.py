import random

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
        
#PARÂMETROS: o tabuleiro e o número de navios
def criar_tabuleiro(matriz,N):
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

            print(f"{matriz[i][j]:4}", end="")
        print("")
    return matriz