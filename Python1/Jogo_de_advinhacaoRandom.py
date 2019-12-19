#Jogo de advinhação com numeros aleatorios
def jogar():
    import random
    print("Bem-vindo ao jogo de advinhacao")
    print("Se errar morre!!!")

    #a linha abaixo gera um numero par aleatorio em um intervalo de 0 a 100
    #caso voce queira gerar apenas numeros aleatorios de 0 a 100 faca random.randrange(0,101)
    n_adv = random.choice(range(0,100,2))

    tentativasTotais = 3
    rodada = 1
    for rodada in range(1, tentativasTotais+1):
        print(rodada , "de", 3)
        chute = input("Digite um numero de 0 a 100: ")
        chute = int(chute)
        print(chute, "esse e o seu chute")
        if(chute<1 or chute>100):
            break
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
    print("O numero secreto e {}, mais sorte na próxima".format(n_adv))
