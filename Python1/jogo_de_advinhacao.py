#Jogo da Advinhação com For
def jogar():
    print("Bem-vindo ao jogo de advinhacao")
    print("Se errar morre!!!")

    n_adv = 17

    tentativasTotais = 3
    rodada = 1
    for rodada in range(1, tentativasTotais+1):
        print(rodada , "de", 3)
        chute = input("Digite um numero: ")
        chute = int(chute)
        print(chute, "esse e o seu chute")

        if(chute == n_adv):
            print("Parabens, voce acertou")
            break
        else:
            if(chute > n_adv):
                print("O numero digitado e maior que o numero secreto, tente um numero menor")
            if(chute < n_adv):
                print("Voce errou, o numero secreto e maior")

        rodada +=1
    print("Fim de Jogo")
    print("O numero secreto e 17, mais sorte na proxima")   
