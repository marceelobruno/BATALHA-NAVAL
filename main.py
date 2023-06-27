import random
import functions_APE

matriz = [[0 for i in range(8)] for i in range(8)]
N = int(input("Digite o numero de navios: "))

tabuleiro_1 = str(functions_APE.criar_tabuleiro(matriz,N))

file_player_1 = open('tabuleiros\jogador1.txt','w')
file_player_1.write(tabuleiro_1)
file_player_1.close()

file_player_2=open('tabuleiros\jogador1.txt','r')
teste = file_player_2.read().replace("'","")
teste2 = list(teste)
print(type(teste2))
print(len(teste2))

matriz_teste = [[0 for i in range(8)] for i in range(8)]

for  i in range(len(teste2)):
    for  j in range(len(teste2)):
        if teste2[i][j] == "A" :
            matriz_teste[i][j] = "A"
        elif teste2[i][j] == "N" :
            matriz_teste[i][j] = "N"
        
for i in range(8):
    for j in range(8):
        print(f'{matriz_teste[i][j]:4}',end="")
    print()


file_player_2.close()




