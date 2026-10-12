import pygame
import random

# constantes 
LARGURA, ALTURA = 1200, 600 #tamanho da tela
TAM_QUADRADO = 20 
VELOCIDADE_JOGO = 15 #velocidade de atualização do jogo

#cores para o jogo
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)

#função para gerar a comida
def gerar_comida():
    comida_x = random.randrange(0, LARGURA, TAM_QUADRADO)
    comida_y = random.randrange(0, ALTURA, TAM_QUADRADO)
    return comida_x, comida_y

#função para fazer o desenho da comida
def desenhar_comida(tela, tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, VERDE, [comida_x, comida_y, tamanho, tamanho])

#função para desenhar a cobrinha
def desenhar_cobra(tela, tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, BRANCO, [pixel[0], pixel[1], tamanho, tamanho])

#função da pontuação
def desenhar_pontuacao(tela, pontuacao):
    fonte = pygame.font.SysFont('Helvetica', 35)
    texto = fonte.render(f'Pontos: {pontuacao}', True, VERMELHO)
    tela.blit(texto, [1, 1])

#função das direções da cobrinha
def selecionar_velocidade(tecla, velocidade_x, velocidade_y):
    if tecla == pygame.K_DOWN and velocidade_y == 0:
        return 0, TAM_QUADRADO
    elif tecla == pygame.K_UP and velocidade_y == 0:
        return 0, -TAM_QUADRADO
    elif tecla == pygame.K_RIGHT and velocidade_x == 0:
        return TAM_QUADRADO, 0
    elif tecla == pygame.K_LEFT and velocidade_x == 0:
        return -TAM_QUADRADO, 0
    return velocidade_x, velocidade_y

#função que contem o jogo a ser chamado no arquivo main.py
def jogar():
    pygame.init()
    pygame.display.set_caption('Jogo Snake Python')
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    relogio = pygame.time.Clock()

    fim_jogo = False
    x = LARGURA // 2
    y = ALTURA // 2
    velocidade_x = 0
    velocidade_y = 0
    tam_cobra = 1
    pixels = []
    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        tela.fill(PRETO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:   # ESC volta ao menu
                    fim_jogo = True
                velocidade_x, velocidade_y = selecionar_velocidade(
                    evento.key, velocidade_x, velocidade_y
                )

        desenhar_comida(tela, TAM_QUADRADO, comida_x, comida_y)

        x += velocidade_x
        y += velocidade_y

        # bateu na parede (verificar depois de mover evita um "frame fantasma")
        if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA:
            fim_jogo = True

        pixels.append([x, y])
        if len(pixels) > tam_cobra:
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        desenhar_cobra(tela, TAM_QUADRADO, pixels)
        desenhar_pontuacao(tela, tam_cobra - 1)
        pygame.display.update()

        if x == comida_x and y == comida_y:
            tam_cobra += 1
            comida_x, comida_y = gerar_comida()

        relogio.tick(VELOCIDADE_JOGO)

    pygame.quit()   # fecha a janela e devolve o controle ao menu