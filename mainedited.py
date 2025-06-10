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


def criar_tabuleiro():
    return [[0 for _ in range(10)] for _ in range(10)]

matrizJogador = criar_tabuleiro()
matrizComputador = criar_tabuleiro()

def printTabuleiroOculto(matriz):
    print("    1 2 3 4 5 6 7 8 9 10")
    print("    ---------------------")
    for i, linha in enumerate(matriz):
        linha_formatada = []
        for celula in linha:
            if celula == 'X' or celula == 'O':
                linha_formatada.append(colorir(celula))
            else:
                linha_formatada.append(colorir('0')) 
        print(f"{i+1:2} -", " ".join(linha_formatada))


def printTabuleiro(matriz):
    print("    1 2 3 4 5 6 7 8 9 10")
    print("    ---------------------")
    for i, linha in enumerate(matriz):
        print(f"{i+1:2} -", " ".join(colorir(str(item)) for item in linha))


def pode_posicionar_navio(matriz, linha, coluna, tamanho, direcao):
    if direcao == 'H':
        if coluna + tamanho > 10:
            return False
        for i in range(tamanho):
            if matriz[linha][coluna + i] != 0:
                return False
    else:
        if linha + tamanho > 10:
            return False
        for i in range(tamanho):
            if matriz[linha + i][coluna] != 0:
                return False
    return True

def posicionar_navio(matriz, linha, coluna, tamanho, direcao, simbolo):
    if direcao == 'H':
        for i in range(tamanho):
            matriz[linha][coluna + i] = simbolo
    else:
        for i in range(tamanho):
            matriz[linha + i][coluna] = simbolo

def gerar_tabuleiro_computador():
    navios = {
        'D': 1,  
        'S': 2,  
        'C': 3,  
        'T': 4,  
        'P': 5   
    }

    matriz = criar_tabuleiro()

    for letra, tamanho in navios.items():
        while True:
            direcao = randint(0, 1) # 0 para horizontal, 1 para vertical
            if direcao == 0: # Horizontal
                linha = randint(0, 9)
                coluna = randint(0, 10 - tamanho)
                if pode_posicionar_navio(matriz, linha, coluna, tamanho, 'H'):
                    posicionar_navio(matriz, linha, coluna, tamanho, 'H', letra)
                    break
            else:  # Vertical
                linha = randint(0, 10 - tamanho)
                coluna = randint(0, 9)
                if pode_posicionar_navio(matriz, linha, coluna, tamanho, 'V'):
                    posicionar_navio(matriz, linha, coluna, tamanho, 'V', letra)
                    break
    return matriz

def obter_jogada_valida():
    while True:
        try:
            jogada = input("Digite onde você quer atacar (LINHA COLUNA): ").split()
            if len(jogada) != 2:
                print("Entrada inválida. Por favor, digite a linha e a coluna separadas por um espaço.")
                continue
            jogadaLinha = int(jogada[0])
            jogadaColuna = int(jogada[1])

            if not (1 <= jogadaLinha <= 10 and 1 <= jogadaColuna <= 10):
                print("Coordenadas fora do tabuleiro. As linhas e colunas devem estar entre 1 e 10.")
                continue
            return jogadaLinha, jogadaColuna
        except ValueError:
            print("Entrada inválida. Por favor, digite números para a linha e a coluna.")

def jogadaJogador(matrizpc):
    while True: 
        jogadaLinha, jogadaColuna = obter_jogada_valida()
        
        celula_alvo = matrizpc[jogadaLinha - 1][jogadaColuna - 1]

        if celula_alvo != 0 and celula_alvo != 'X' and celula_alvo != 'O':
            print("Você acertou algo!")
            matrizpc[jogadaLinha - 1][jogadaColuna - 1] = 'X'
            printTabuleiroOculto(matrizpc)
            return True # Acertou um navio
        elif celula_alvo == 0:
            print("Você acertou a água!")
            matrizpc[jogadaLinha - 1][jogadaColuna - 1] = 'O'
            printTabuleiroOculto(matrizpc)
            return False # Acertou a água
        elif celula_alvo == 'O' or celula_alvo == 'X':
            print("Você já jogou nesse lugar! Jogue novamente!")

def jogadaComputador(matrizJogador, tentativas_computador):
    while True:
        jogadaLinha, jogadaColuna = randint(1, 10), randint(1, 10)
        if (jogadaLinha, jogadaColuna) in tentativas_computador:
            continue
        
        tentativas_computador.append((jogadaLinha, jogadaColuna))
        celula_alvo = matrizJogador[jogadaLinha - 1][jogadaColuna - 1]

        if celula_alvo != 0 and celula_alvo != 'X' and celula_alvo != 'O':
            print(f"O computador atacou em ({jogadaLinha}, {jogadaColuna}) e acertou algo!")
            matrizJogador[jogadaLinha - 1][jogadaColuna - 1] = 'X'
            printTabuleiro(matrizJogador)
            return True # Acertou um navio
        elif celula_alvo == 0:
            print(f"O computador atacou em ({jogadaLinha}, {jogadaColuna}) e acertou a água!")
            matrizJogador[jogadaLinha - 1][jogadaColuna - 1] = 'O'
            printTabuleiro(matrizJogador)
            return False # Acertou a água

def todos_navios_afundados(matriz):
    navios_restantes = ['D', 'S', 'C', 'T', 'P']
    for linha in matriz:
        for celula in linha:
            if celula in navios_restantes:
                return False
    return True

def configurar_navios_jogador(matrizJogador):
    navios = {
        'D': 1,  
        'S': 2,  
        'C': 3,  
        'T': 4,  
        'P': 5   
    }

    print("\n--- POSICIONAMENTO DOS SEUS NAVIOS ---")
    for letra, tamanho in navios.items():
        while True:
            printTabuleiro(matrizJogador)
            print(f"Posicione seu navio {letra} (Tamanho: {tamanho})")
            try:
                entrada = input("Digite a linha, coluna e direção (H para Horizontal, V para Vertical): ").upper().split()
                if len(entrada) != 3:
                    print("Entrada inválida. Use o formato: LINHA COLUNA DIRECAO (ex: 1 1 H)")
                    continue
                linha = int(entrada[0]) - 1
                coluna = int(entrada[1]) - 1
                direcao = entrada[2]

                if not (0 <= linha <= 9 and 0 <= coluna <= 9):
                    print("Coordenadas fora do tabuleiro. Tente novamente.")
                    continue
                if direcao not in ['H', 'V']:
                    print("Direção inválida. Use 'H' para Horizontal ou 'V' para Vertical.")
                    continue

                if pode_posicionar_navio(matrizJogador, linha, coluna, tamanho, direcao):
                    posicionar_navio(matrizJogador, linha, coluna, tamanho, direcao, letra)
                    break
                else:
                    print("Não é possível posicionar o navio aqui. Verifique se há espaço suficiente ou se não há sobreposição.")
            except ValueError:
                print("Entrada inválida. Certifique-se de digitar números para linha e coluna.")

def jogar_batalha_naval():
    global matrizJogador, matrizComputador
    while True:
        matrizJogador = criar_tabuleiro()
        matrizComputador = gerar_tabuleiro_computador()
        tentativas_computador = []

        configurar_navios_jogador(matrizJogador)

        print("\n--- INÍCIO DO JOGO ---")
        while True:
            print("\n--- SEU TABULEIRO ---")
            printTabuleiro(matrizJogador)
            print("\n--- TABULEIRO INIMIGO (OCULTO) ---")
            printTabuleiroOculto(matrizComputador)

            print("\nSUA VEZ DE ATACAR!")
            jogadaJogador(matrizComputador)

            if todos_navios_afundados(matrizComputador):
                print("PARABÉNS! VOCÊ DESTRUIU TODOS OS NAVIOS INIMIGOS E VENCEU A BATALHA!")
                break

            print("\nVEZ DO COMPUTADOR!")
            jogadaComputador(matrizJogador, tentativas_computador)

            if todos_navios_afundados(matrizJogador):
                print("QUE PENA! O COMPUTADOR DESTRUIU TODOS OS SEUS NAVIOS. VOCÊ PERDEU A BATALHA!")
                break

        print("\nFIM DE JOGO.")
        while True:
            jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
            if jogar_novamente in ['s', 'n']:
                break
            else:
                print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")
        if jogar_novamente == 'n':
            break

if __name__ == "__main__":
    jogar_batalha_naval()


