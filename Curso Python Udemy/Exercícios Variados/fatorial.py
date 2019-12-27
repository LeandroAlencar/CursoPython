#5! = 5.4.3.2.1
valor = int(input('Digite um número inteiro positivo: '))
cont = valor
num = 1
print('{}! = ' .format(valor), end='')

#Solução1 - UTILIZANDO WHILE
while cont > 0:
    print('{}'.format(cont), end = '')
    print(' x ' if cont>1 else' = ', end='')
    num *= cont
    cont -= 1
print('{}' .format(num))

#SOLUÇÃO2 - UTILIZANDO FOR

for j in range (1,valor+1):
    print('{}'.format(j), end='')
    print(' x ' if j<valor else' = ', end='')
    num *= j
print('{}' .format(num))

#SOLUÇÃO 3 - UTILIZANDO FOR E LIST
lista = list(range(1,valor+1))
for ind, item in enumerate(lista):
    print('{}'.format(lista[ind]), end='')
    print(' x ' if lista[ind]<lista[-1] else' = ', end='')
    num *= lista[ind]
print(num)
