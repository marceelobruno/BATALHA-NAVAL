from functions_APE import *

while True:
    N = int(input("Digite o numero de navios: (1 - 6)"))
    if N <= 6 and N > 0:
        break
    else:
        print("Insira um valor válido entre 1 e 6")

jogador1 = gerar_tabuleiro(N)
jogador2 = gerar_tabuleiro(N)

test = menu(jogador1, jogador2)
while test:
    if test:
        event = 0
        tab_1 = [["X" for i in range(8)] for i in range(8)]
        tab_2 = [["X" for i in range(8)] for i in range(8)]

        exibir_game(tab_1, tab_2)

        while True:
            print()
            print("Para acessar o menu digite: 8")
            print()
            print("Vez do jogador 1")
            print()

            linha = int(input("Digite a posição da linha"))
            if linha == 8: 
                menu(jogador1, jogador2)
                break
            coluna = int(input("Digite a posição da coluna"))

            if linha < 8 and coluna < 8:
                if jogador1[linha][coluna] == "N":
                    tab_1[linha][coluna] = 'N'

                    print("""

                    #########   FOGO   ##########
                    
                    """)

                    exibir_game(tab_1, tab_2)
                else: 

                    print("""

                    #########   AGUA   ##########

                    """)

                    tab_1[linha][coluna] = 'A'
                    exibir_game(tab_1, tab_2)

            else:
                print("Digite um valor válido")
                print()
                print("Perdeu a vez")
                print()

            print()
            print("Para acessar o menu digite: 8")
            print()
            print("Vez do jogador 2")
            print()

            linha = int(input("Digite a posição da linha"))
            if linha == 8: 
                menu(jogador1, jogador2)
                break
            coluna = int(input("Digite a posição da coluna"))

            if linha < 8 and coluna < 8:
                if jogador1[linha][coluna] == "N":
                    tab_2[linha][coluna] = 'N'

                    print("""

                    #########   FOGO   ##########

                    """)

                    exibir_game(tab_1, tab_2)
                else: 

                    print("""

                    #########   AGUA   ##########

                    """)

                    tab_2[linha][coluna] = 'A'
                    exibir_game(tab_1, tab_2)
            else:
                print("Digite um valor válido")
                print()
                print("Perdeu a vez")
                print()
    else:
        print("Você encerrou o programa !!")



        






