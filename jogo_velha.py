import questionary
import os #biblioteca do sistema operacional

#função para limpar o terminal
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') 

#função que chama o titulo
def titulo():    
    print(' ==========================================')
    print('              JOGO DA VELHA                ')
    print(' ==========================================')

# Cria o tabuleiro com 9 posicoes vazias
tabuleiro = ["", "", "",
             "", "", "",
             "", "", ""]

# O jogador X comeca
jogador = "X"


#função para que realizar ocupações no tabuleiro
def jogo(posicao):
    global jogador

    # Verifica se a posicao existe
    if posicao < 0 or posicao > 8:
        return False

    # Verifica se a posicao esta vazia
    if tabuleiro[posicao] == "":

        # Coloca X ou O na posicao escolhida
        tabuleiro[posicao] = jogador

        # Troca o jogador
        jogador = 'O' if jogador == 'X' else 'X'
        return True

    # Se a posicao ja estiver ocupada
    else:
        return False


#função que verifica vencedor
def verificar_vencedor():

# Linhas
    linhas = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),   # linhas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),   # colunas
        (0, 4, 8), (2, 4, 6),              # diagonais
    ]
    for a, b, c in linhas:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] != "":
            return tabuleiro[a]
    return None


#função que verifica se houve empate
def verificar_empate():
    return '' not in tabuleiro and verificar_vencedor() is None


#função que reinicia o jogo
def reiniciar():
    global tabuleiro, jogador

    # Limpa o tabuleiro
    tabuleiro = ["", "", "",
                 "", "", "",
                 "", "", ""]

    # X volta a ser o primeiro jogador
    jogador = "X"      

#função para denhar tabuleiro
def desenhar_tabuleiro():
    print()
    print(tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
    print("--+---+--")
    print(tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
    print("--+---+--")
    print(tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])
    print()

#função para escolher posições
def escolher_posicao():
    opcoes = []
    for i in range (9):
        conteudo = tabuleiro[i]
        rotulo = f'Posição {i+1}' + (f' opucado por ' if conteudo else '')
        opcoes.append(
            questionary.Choice(rotulo, value = i, disabled = f'{conteudo}' if conteudo else False)
        )

    return questionary.select(
        'Escolha a posição: ',
        choices = opcoes,
        qmark = '',
    ).ask()

#função para chamar o jogo no arquivo main.py
def jogar():
    reiniciar()
    limpar()
    titulo()

    while True:
        limpar()
        titulo()
        desenhar_tabuleiro()
        print("Vez do jogador:", jogador)

        posicao = escolher_posicao()

        if posicao is None: #Ctrl+C fecha o jogo
            return

        jogo(posicao)

        vencedor = verificar_vencedor()

        if vencedor is not None:
            limpar()
            titulo()
            desenhar_tabuleiro()
            print("O jogador", vencedor, "VENCEU!")
            return

        if verificar_empate():
            limpar()
            titulo()
            desenhar_tabuleiro()
            print("\nDEU VELHA!")
            input('\nPressione ENTER para voltar ao menu')
            return

        
