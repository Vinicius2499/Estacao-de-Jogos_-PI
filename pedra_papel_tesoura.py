import os #biblioteca do sistema operacional

#função para limpar o terminal
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') 

#função que redesenha o título no terminal após limpeza 
def titulo():
    print("================================")
    print(" PEDRA, PAPEL e TESOURA 🎮")
    print("================================")

#função para chama o jogo no arquivo main.py
def jogar():
    limpar()
    titulo()
    import random
    import questionary #para que o usuário selecione as jogadas pelas setas do teclado
    escolhas = ["pedra", "papel", "tesoura"]

    vence = {
        'pedra' : 'tesoura',
        'papel' : 'pedra',
        'tesoura' : 'papel'
    }

    #emojis para o resultado
    emojis = {
        "pedra": "🪨 ",
        "papel": "📄",
        "tesoura": "✂️ ", 
    }
    #menu de escolhar do jogo
    while True:
        limpar()
        titulo()

        #menu de escolhas de jogadas do usuário
        jogador = questionary.select(
            'Escolha sua jogada: ', #esse é o titulo do menu
            choices = [             #apresenta as escolhas
                questionary.Choice("🪨  Pedra", value = "pedra"),
                questionary.Choice("📄 Papel", value = "papel"),
                questionary.Choice("✂️  Tesoura", value = "tesoura")
            ], 
            qmark = '✊', #adiciona o emoji na mensagem de escolhas
            instruction = '(Use as setas do teclado)' #instrução ao usuário
        ).ask()
        # Ctrl+C  no questionary retorna None e volta ao menu
        if jogador is None:
            return 
        
        computador = random.choice(escolhas) #escolha aleatória do computador

        #exibição dos resultados
        print(f"\nVocê escolheu: {emojis[jogador]} {jogador}\n")
        print(f"Computador escolheu: {emojis[computador]} {computador}\n")

        if jogador == computador:
            print("Empate!")
            
        elif vence[jogador] ==  computador:
            print("Você ganhou!")

        else:
            print("Você perdeu!")

        #permite o jogador escolher se quer jogar novamente
        de_novo = questionary.confirm(
            '\nJogar de novo?\n',
            qmark = ' ',
            auto_enter = False 
            ).ask() 
        if not de_novo:
            return #volta ao menu

