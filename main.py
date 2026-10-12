import questionary #biblioteca que permite escolha pelas setas do computador
import time #biblioteca para animação de encerramento e carregamento
import snake, jogo_forca, jogo_velha, pedra_papel_tesoura #arquivo dos jogos
import os #biblioteca do sistema operacional
import sys 

#função para limpar a tela
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') #essa linha serve para permitir limpar o teminal no windowns e linux

#função para encerrar o programa
def sair():
    print('\nENCERRANDO PROGRAMA', end='', flush=True)
    for i in range(3):
        time.sleep(0.5)
        print('.', end='', flush=True)
    print()
    limpar()
    sys.exit()

#lista de jogos para o menu/ o ".jogar" é uma função que chama os jogos
jogos = {
    "🐍 Snake": snake.jogar,
    "🔤 Jogo da Forca": jogo_forca.jogar,
    "❌ Jogo da Velha": jogo_velha.jogar,
    "✊ Pedra, Papel e Tesoura": pedra_papel_tesoura.jogar,
    "🚪 Sair" : sair
}


#essa é a configuração do menu dos jogos
def menu():
    limpar()
    while True:
        escolha = questionary.select(
            'Estação de Jogos - escolha um jogo ', #título da estação
            choices = list(jogos.keys()), #apresenta as escolhas de jogos ao usuário
            qmark = '🎮',
            instruction = '(Use as setas do teclado)'
        ).ask()

        #encerra o programa caso o usuário selecione sair ou aperte Ctrl+C
        if escolha is None or escolha ==  '🚪 Sair':
            sair()

        print('\nEXECUTANDO OPÇÃO',end = '', flush = True)
        for i in range (3):
            print('.', end = '', flush = True)
            time.sleep(0.3)

        print()
        limpar()

        jogos[escolha]()

        input('\nPressione ENTER para voltar ao menu')
        limpar()

if __name__ == '__main__':
    menu()