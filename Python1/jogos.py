import Jogo_de_advinhacaoRandom
import jogo_de_advinhacao

print('advinhação (1), advinhaçãoBacana(2)')

n = int (input("Qual jogo voce deseja jogar?"))
if n == 2:
    print("Loading...")
    Jogo_de_advinhacaoRandom.jogar()

if n==1:
    print("Loading...")
    jogo_de_advinhacao.jogar()