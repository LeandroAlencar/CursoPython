import random 
from time import sleep
itens = ['PAPEL','PEDRA','TESOURA']
cpu = 0
jogador = 0
tent = 0
jogada = 0
rodadas = 0
escolha = 'não'
empates = 0
print('BEM-VINDO AO PEDRA PAPEL E TESOURA!')
nome = input('Insira seu nome: ')
print('(0) PAPEL, (1) PEDRA, (2) TESOURA')

while escolha!='sim':
    tent = int(input('Faça a sua jogada: '))
    jogada = random.choice(range(0,3,1))
    print('JO')
    sleep(1)#Para dar um delay de um segundo
    print('KEN')
    sleep(1)
    print('PO!')
    sleep(1)
    print('CPU jogou {}' .format(itens[jogada]))
    print('-+'*12)
    print('{} jogou {}' .format(nome,itens[tent]))

    if jogada == tent:
        print('Jogo Empatado')
        empates+=1
    elif jogada == 0:
        if tent == 1:
            print('CPU venceu!')
            cpu+=1
        if tent == 2:
            print('{} venceu!'.format(nome))
            jogador+=1
    elif jogada == 1:
        if tent == 2:
            print('CPU venceu!')
            cpu+=1
        if tent == 0:
            print('{} venceu!' .format(nome))
            jogador+=1
    elif jogada == 2:
        if tent == 0:
            print('CPU venceu!')
            cpu+=1
        if tent == 1:
            print('{} venceu!' .format(nome))
            jogador+=1
    else:
        print('Faça uma jogada válida,{}!' .format(nome))
    rodadas+=1
    escolha = input('Deseja Sair ,{} ? ' .format(nome))

print('FIM DE JOGO')
print('PONTUAÇÃO:')
print('{}: {}, CPU: {}' .format(nome,jogador,cpu))
if jogador > cpu:
    print('{} venceu' .format(nome))
elif jogador == cpu:
    print('Jogo empatado')
else:
    print('CPU venceu')
print('Rodadas Jogadas {}:' .format(rodadas))
print('Empates {}:'.format(empates))