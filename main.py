from time import sleep
from random import randint

RESET = '\033[0m'
VERMELHO = '\033[91m'
AZUL = '\033[94m'
VERDE = '\033[92m'
AMARELO = '\033[93m'
ROXO = '\033[95m'
BRANCO = '\033[97m'
ROSA = '\033[35m'


def colorir(celula):
    if celula == 'D':
        return f"{AMARELO}D{RESET}"
    elif celula == 'T':
        return f"{VERDE}T{RESET}"
    elif celula == 'C':
        return f"{ROXO}C{RESET}"
    elif celula == 'S':
        return f"{ROSA}S{RESET}"
    elif celula == 'P':
        return f"{BRANCO}P{RESET}"
    elif celula == 'X':
        return f"{VERMELHO}X{RESET}"
    elif celula == '0':
        return f"{AZUL}O{RESET}"
    else:
        return f"{celula}"


matrizJogador = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

matrizComputador = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def printTabuleiro(matriz):
    cont = 0
    print("    1 2 3 4 5 6 7 8 9 10")
    print("    --------------------")
    for linha in matriz:
        cont += 1
        print(f"{cont:2} -", " ".join(colorir(str(item)) for item in linha))
    
def gerar_tabuleiro_computador():
    navios = {
        'D': 1,  
        'S': 2,  
        'C': 3,  
        'T': 4,  
        'P': 5   
    }

    matriz = [[0 for _ in range(10)] for _ in range(10)]

    for letra, tamanho in navios.items():
        while True:
            direcao = randint(0, 1) 
            if direcao == 0: 
                linha = randint(0, 9)
                coluna = randint(0, 10 - tamanho)
                if all(matriz[linha][coluna + i] == 0 for i in range(tamanho)):
                    for i in range(tamanho):
                        matriz[linha][coluna + i] = letra
                    break
            else:  
                linha = randint(0, 10 - tamanho)
                coluna = randint(0, 9)
                if all(matriz[linha + i][coluna] == 0 for i in range(tamanho)):
                    for i in range(tamanho):
                        matriz[linha + i][coluna] = letra
                    break

    return matriz


print("TABULEIRO DO JOGADOR")
printTabuleiro(matrizJogador)
printTabuleiro(gerar_tabuleiro_computador())

print()
destroierPLinha, destroierPColuna = map(int, input("SELECIONE A POSIÇÃO DO SEU DESTROIER (1x1): [LINHA COLUNA] ").split())
matrizJogador[destroierPLinha - 1][destroierPColuna - 1] = 'D'

printTabuleiro(matrizJogador)

cont = 0
while True:
    print()
    subPLinha, subPColuna = map(int, input("SELECIONE A POSIÇÃO DO SEU SUBMARINO (2x1): [LINHA COLUNA] ").split())
    if matrizJogador[subPLinha - 1][subPColuna - 1] != 0 :
        print("Já tem um navio nessa posição!")
    else:
        matrizJogador[subPLinha - 1][subPColuna - 1] = 'S'
        cont += 1
        printTabuleiro(matrizJogador)
    if cont == 2:
        break

cont = 0
while True:
    print()
    ctPLinha, ctPColuna = map(int, input("SELECIONE A POSIÇÃO DO SEU CONTRATORPEDEIRO (3x1): [LINHA COLUNA] ").split())
    if matrizJogador[ctPLinha - 1][ctPColuna - 1] != 0 :
        print("Já tem um navio nessa posição!")
    else:
        matrizJogador[ctPLinha - 1][ctPColuna - 1] = 'C'
        cont += 1
        printTabuleiro(matrizJogador)
    if cont == 3:
        break


cont = 0
while True:
    print()
    tanquePLinha, tanquePColuna = map(int, input("SELECIONE A POSIÇÃO DO SEU NAVIO TANQUE (4x1): [LINHA COLUNA] ").split())
    if matrizJogador[tanquePLinha - 1][tanquePColuna - 1] != 0 :
        print("Já tem um navio nessa posição!")
    else:
        matrizJogador[tanquePLinha - 1][tanquePColuna - 1] = 'T'
        cont += 1
        printTabuleiro(matrizJogador)
    if cont == 4:
        break

cont = 0
while True:
    print()
    paPLinha, paPColuna = map(int, input("SELECIONE A POSIÇÃO DO SEU PORTA-AVIÕES (5x1): [LINHA COLUNA] ").split())
    if matrizJogador[paPLinha - 1][paPColuna - 1] != 0 :
        print("Já tem um navio nessa posição!")
    else:
        matrizJogador[paPLinha - 1][paPColuna - 1] = 'P'
        cont += 1
        printTabuleiro(matrizJogador)
    if cont == 5:
        break

printTabuleiro(matrizJogador)