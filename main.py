from time import sleep
from random import randint

RESET = '\033[0m'
VERMELHO = '\033[91m'
AZUL = '\033[94m'
VERDE_CLARO = '\033[92m'
AMARELO = '\033[93m'
LARANJA_VIVO = '\033[38;5;208m'
BRANCO = '\033[97m'
ROSA = '\033[35m'
MARROM = '\033[38;5;94m'


def colorir(celula):
    if celula == 'D':
        return f"{AMARELO}D{RESET}"
    elif celula == 'T':
        return f"{VERDE_CLARO}T{RESET}"
    elif celula == 'C':
        return f"{LARANJA_VIVO}C{RESET}"
    elif celula == 'S':
        return f"{ROSA}S{RESET}"
    elif celula == 'P':
        return f"{BRANCO}P{RESET}"
    elif celula == 'X':
        return f"{VERMELHO}X{RESET}"
    elif celula == '0':
        return f"{AZUL}O{RESET}"
    elif celula == 'O':
        return f"{MARROM}O{RESET}"
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

def printTabuleiroOculto(matriz):
    print("    1 2 3 4 5 6 7 8 9 10")
    print("    --------------------")
    for i, linha in enumerate(matriz):
        linha_formatada = []
        for celula in linha:
            if celula == 'X' or celula == 'O':
                linha_formatada.append(colorir(celula))
            else:
                linha_formatada.append(colorir('0')) 
        print(f"{i+1:2} -", " ".join(linha_formatada))



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

def jogadaJogador(matrizpc):
    while True: 
        sleep(2)
        jogadaLinha, jogadaColuna = map(int, input("digite onde voce quer atacar: [LINHA(espaco)COLUNA] ").split())
        sleep(2)
        if matrizpc[jogadaLinha - 1][jogadaColuna - 1] != 0 and matrizpc[jogadaLinha - 1][jogadaColuna - 1] != 'X' and matrizpc[jogadaLinha - 1][jogadaColuna - 1] != 'O':
            print("Você acertou algo...")
            matrizpc[jogadaLinha - 1][jogadaColuna - 1] = 'X'
            printTabuleiroOculto(matrizpc)
            break
        elif matrizpc[jogadaLinha - 1][jogadaColuna - 1] == 0:
            print("Você acertou a água! ")
            matrizpc[jogadaLinha - 1][jogadaColuna - 1] = 'O'
            printTabuleiroOculto(matrizpc)
            break
        elif matrizpc[jogadaLinha - 1][jogadaColuna - 1] == 'O' or matrizpc[jogadaLinha - 1][jogadaColuna - 1] == 'X':
            print("Você já jogou nesse lugar! Jogue novamente!")
    return jogadaLinha, jogadaColuna

def jogadaComputador(matriz):
    while True:
        jogadaLinha, jogadaColuna = randint(1, 10), randint(1, 10)
        if matriz[jogadaLinha - 1][jogadaColuna - 1] != 0 and matriz[jogadaLinha - 1][jogadaColuna - 1] != 'X' and matriz[jogadaLinha - 1][jogadaColuna - 1] != 'O':
            print("O computador acertou algo...")
            matriz[jogadaLinha - 1][jogadaColuna - 1] = 'X'
            printTabuleiro(matriz)
        elif matriz[jogadaLinha - 1][jogadaColuna - 1] == 0:
            print("O computador acertou a água! ")
            matriz[jogadaLinha - 1][jogadaColuna - 1] = 'O'
            printTabuleiro(matriz)
            break
        elif matriz[jogadaLinha - 1][jogadaColuna - 1] == 'O' or matriz[jogadaLinha - 1][jogadaColuna - 1] == 'X':
            continue
        printTabuleiro(matriz)
    return jogadaLinha, jogadaColuna
        
def checkSub(matriz):
    for linha in matriz:
        if 'S' in linha:
            return False
    return True

def checkContratorp(matriz):
    for linha in matriz:
        if 'C' in linha:
            return False
    return True

def checkDes(matriz):
    for linha in matriz:
        if 'D' in linha:
            return False
    return True

def checkTanque(matriz):
    for linha in matriz:
        if 'T' in linha:
            return False
    return True

def checkPortA(matriz):
    for linha in matriz:
        if 'P' in linha:
            return False
    return True

print("TABULEIRO DO JOGADOR")
printTabuleiro(matrizJogador)
matrizComputador = gerar_tabuleiro_computador()

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

destruidoDes = False
destruidoSub = False
destruidoContratorp = False
destruidoPortA = False
destruidoTanque = False

while True:
    jogadaJogador(matrizComputador)
    if checkDes(matrizComputador) == True and destruidoDes == False:
        print("Você destruiu o Destroier Inimigo!!")
        destruidoDes == True
    if checkContratorp(matrizComputador) == True and destruidoContratorp == False:
        print("Você destruiu o Contratorpedeiro Inimigo!!")
        destruidoContratorp = True
    if checkSub(matrizComputador) == True and destruidoSub == False:
        destruidoSub = True
        print("Você destruiu o Submarino inimigo!!")
    if checkTanque(matrizComputador) == True and destruidoTanque == False:
        destruidoTanque = True
        print("Você destruiu o Navio Tanque inimigo!!")
    if checkPortA(matrizComputador) == True and destruidoPortA == False:
        destruidoPortA = True
        print("Você destruiu o Porta Aviões do inimigo!!")
    sleep(2)
    print("VEZ DO COMPUTADOR")
    sleep(2)
    jogadaComputador(matrizJogador)
    sleep(2)
    
