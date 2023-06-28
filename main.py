from functions_APE import *

with open('art_generator.txt', 'r') as arquivo:
    print(arquivo.read())

while True:
    N = int(input("Digite o número de navios (1 - 6): "))
    if N <= 6 and N > 0:
        break
    else:
        print("Insira um valor válido entre 1 e 6!")

print('Informe os nomes dos jogadores:')
jogador1_nome = input('Jogador 1: ').title()
jogador2_nome = input('Jogador 2: ').title()

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

            # Jogador 1
            print(f"\nVez do jogador 1 - {jogador1_nome}")
            print()

            linha = int(input("Digite a posição da linha: "))
            if linha == 8:
                menu(jogador1, jogador2)
                break
            coluna = int(input("Digite a posição da coluna: "))

            if linha < 8 and coluna < 8:
                if jogador1[linha][coluna] == "N":
                    tab_1[linha][coluna] = 'N'

                    print("""

                    #########   FOGO   ##########
                    
                    """)

                    exibir_game(tab_1, tab_2)
                else:

                    print("""

                    #########   ÁGUA   ##########

                    """)

                    tab_1[linha][coluna] = 'A'
                    exibir_game(tab_1, tab_2)

            else:
                print("Digite um valor válido.")
                print()
                print("Perdeu a vez!")
                print()

            print()
            print("Para acessar o menu digite: 8")

            # Jogador 2
            print(f"\nVez do jogador 2 - {jogador2_nome}")
            print()

            linha = int(input("Digite a posição da linha: "))
            if linha == 8:
                menu(jogador1, jogador2)
                break

            coluna = int(input("Digite a posição da coluna: "))

            if linha < 8 and coluna < 8:
                if jogador1[linha][coluna] == "N":
                    tab_2[linha][coluna] = 'N'

                    print("""

                    #########   FOGO   ##########

                    """)

                    exibir_game(tab_1, tab_2)
                else:

                    print("""

                    #########   ÁGUA   ##########

                    """)

                    tab_2[linha][coluna] = 'A'
                    exibir_game(tab_1, tab_2)
            else:
                print("Digite um valor válido.")
                print()
                print("Perdeu a vez!")
                print()
    else:
        print("Você encerrou o programa !!")
