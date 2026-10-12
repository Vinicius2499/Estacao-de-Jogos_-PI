import questionary
import os
import sys
import unicodedata
import time
import random            

def limpar():
        os.system('cls' if os.name == 'nt' else 'clear')

def imprime_mensagem_abertura():
        print('===================================')
        print('== Bem-vindo(a) ao jogo da Forca ==')
        print('===================================\n')

#função para normalizar acentos e o usuário conseguir acertar sem precisar escrever o acento
def normalizar(texto):
    sem_acento = unicodedata.normalize('NFKD', texto)
    return''.join(c for c in sem_acento if not unicodedata.combining(c)).upper()

def carrega_palavra_secreta():
        palavras = [
                'MAÇÃ', 'UVA', 'LARANJA', 'LIMÃO', 'CENOURA', 'PEPINO', 'PIZZA', 'CASA', 'PRÉDIO', 'PROFESSOR',
                'QUARTO', 'CADEIRA', 'PROGRAMA', 'ESTRELA', 'ANJO', 'MESA', 'LETRA', 'PALAVRA', 'LIVRO', 'TECLADO', 'TELHADO', 'CARRO',
                'MOTOR', 'RODA', 'BUZINA', 'MUSICA', 'BANDA', 'SHOW', 'ALTO', 'BAIXO', 'COMPUTADOR', 'GATO', 'CACHORRO', 'PATO','GALINHA',
                'CAVALO', 'HUMANO', 'VACA', 'VIZINHO', 'AMIGO', 'MÃE', 'PAI', 'IRMÃO', 'PRIMA', 'IRMÃ', 'TRISTE', 'FELIZ', 'SAÚDE',
                'JOGO', 'SEGREDO', 'HISTÓRIA', 'GEOGRAFIA', 'EDUCAÇÃO', 'ESCOLA', 'HOSPITAL', 'DELEGACIA', 'POLICIAL', 'MÉDICO', 'BOMBEIRO',
                'CAMINHÃO', 'CAMINHO', 'RUA', 'ESTRADA', 'DIVERSÃO', 'BEBIDA', 'COMIDA', 'SORVETE', 'ARROZ', 'ÀGUA', 'FOGO', 'TERRA', 'VENTO',
                'CABEÇA', 'BRAÇO', 'MÃO', 'PERNA', 'BARRIGA', 'PÉ', 'ESPELHO', 'ARMÁRIO', 'PÔSTER', 'CAMA', 'TRAVESSEIRO', 'ÔNIBUS', 'AVÔ', 'AVÓ'
                ]
        
        return random.choice(palavras)
        
def inicializa_letras_acertadas(palavra):
        return['_' for _ in palavra]
        
def pede_chute(letras_chutadas, erros, letras_acertadas):
    while True:
        limpar()
        imprime_mensagem_abertura()
        desenha_forca(erros)
        print(' '.join(letras_acertadas))
        imprime_letras_chutadas(letras_chutadas)

        chute = input('\nDigite uma letra: ').strip().upper()
        if len(chute)!= 1 or not chute.isalpha():
            print('Digite apenas uma letra!')
            time.sleep(1.5)
            continue

        chute_normalizado = normalizar(chute)

        if chute_normalizado in letras_chutadas:
            print(f'Você já escolheu a letra {chute}. Tente outra!')
            time.sleep(1.5)
            continue

        return chute, chute_normalizado
        
def marca_chute_correto(chute_normalizado, letras_acertadas, palavra_secreta):
        acertou_alguma = False
        for index, letra in enumerate(palavra_secreta):
                if normalizar(letra) == chute_normalizado:
                    letras_acertadas[index] = letra
                    acertou_alguma = True

        return acertou_alguma

def imprime_letras_chutadas(letras_chutadas):
      if letras_chutadas:
        print('\nLetras já escolhidas:', ' '.join(sorted(letras_chutadas)))

def desenha_forca(erros):
        estagios = [
                          """
                  ___
                 |/ |
                 |
                 |
                 |
                 |
                 |__
                 """,
                          """
                  ___
                 |/ |
                 | (_)
                 |
                 |
                 |
                 |__
                 """,
                          """
                  ___
                 |/ |
                 | (_)
                 |  |
                 |
                 |
                 |__
                 """,
                          """
                  ___
                 |/ |
                 | (_)
                 |--|--
                 |
                 |
                 |__
                 """,
                          """
                  ___
                 |/ |
                 | (_)
                 |--|
                 |
                 |
                 |__
                 """,
                          """
                  ___
                 |/ |
                 | (_)
                 |--|--
                 |  |
                 |
                 |__
                 """,
                 """
                  ___
                 |/ |
                 | (_)
                 |--|--
                 |  |
                 | |
                 |__
                 """,
                 """
                  ___
                 |/ |
                 | (_)
                 |--|--
                 |  |
                 | | |
                 |__
                 """
                        ]
        print (estagios [erros])  
                                                       
def imprime_mensagem_vencedor():
        print ('\n* PARABÉNS!!! Você acertou!! (^-^) *')
        
def imprime_mensagem_perdedor(palavra_secreta):
        print (f'Poxa, você foi enforcado!! (T-T)\n A palavra era {palavra_secreta}.')


def jogo():
    limpar()
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    letras_chutadas = set()

    erros = 0
    acertou = False
    enforcou = False      
    while not acertou and not enforcou:
        chute, chute_normalizado = pede_chute(letras_chutadas, erros, letras_acertadas)
        letras_chutadas.add(chute_normalizado)

        if not marca_chute_correto(chute_normalizado, letras_acertadas, palavra_secreta):
            erros += 1
        
        enforcou = erros == 7
        acertou = '_' not in letras_acertadas

    print(' '.join(letras_acertadas))
    
    if acertou:
        limpar()
        imprime_mensagem_abertura()
        imprime_mensagem_vencedor()
        print('\nA palavra era', palavra_secreta)
        return True
    else:
        limpar()
        imprime_mensagem_abertura()
        imprime_mensagem_perdedor(palavra_secreta)
        return False

def jogar():
    vitorias = 0
    derrotas = 0
    while True:
        if jogo():
            vitorias += 1 
        else:
            derrotas += 1

        print(f'\nPlacar da sessão - Vitórias: {vitorias} | Derrotas: {derrotas}')

        de_novo = questionary.confirm('\nJogar novamente?', qmark ='').ask()
        if not de_novo:
            return


