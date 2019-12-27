import random
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
cpu = 0
jogador = 0
escolha = 'não'
print(' BEM-VINDO AO PEDRA PAPEL E TESOURA!')
print('(0) PAPEL, (1) PEDRA, (2) TESOURA')


while escolha != 'sim':
    tent = int(input('Faça a sua jogada: '))
    jogada = random.choice(range(0,3,1))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!')
    sleep(1)
    if tent == 0 and jogada == 1:
        print('Você venceu!')
        jogador += 1
    elif tent == 0 and jogada ==2:
        cpu +=1
    elif tent == 0 and jogada == 0:
        print('Jogo empatado!')
    elif tent == 1 and jogada == 2:
        print('Você Venceu!')
        jogador +=1
    elif tent == 1 and jogada == 1:
        print('Jogo Empatado!')
    elif tent == 1 and jogada == 0:
        print('Você perdeu!')
        cpu +=1
    elif tent == 2 and jogada == 2:
        print('Jogo Empatado!')
    elif tent == 2 and jogada == 0:
        print('Você Venceu!')
        jogador +=1
    elif tent == 2 and jogada == 1:
        print('Você Perdeu!')
        cpu +=1
    else:
        print('Escolha uma das opções dadas!')
    escolha = input('Deseja Sair? ')


print('FIM DE JOGO')
print('PONTUAÇÃO:')
print('JOGADOR: {}, CPU: {}' .format(jogador,cpu))
if jogador > cpu:
    print('jogador venceu')
elif jogador == cpu:
    print('Jogo empatado')
else:
    print('cpu venceu')