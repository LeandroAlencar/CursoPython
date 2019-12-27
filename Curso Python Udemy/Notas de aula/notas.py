"""
a = 10
b = 20
print(a,b)
print()

a,b = b,a#Trocando os valores 
print(a,b)

#Atribuição múltipla
x,y,z = 2,4,6# x recebe 2, y recebe 4 e z recebe 6
print(z,y,x)

#Também podemos fazer atribuiçôes múltiplas utilizando operações matemáticas

x,y,z = x*2, y**2,z*10 #A parte a direita da igualdade será executada primeiro, depois o programa atribui
print(z,y,x)
"""
"""
#Atribuição condicional colocarmos um determinado dado em uma variável se uma determinada ação ocorrer

x = 9
texto = 'sim' if x == 10 else 'não'
print(texto)

num = int(input('Digite um número qualquer:'))
res = 'par' if num%2 == 0 else 'ímpar'
print('O número digitado é: ' res)
"""
"""
x = 0
while x<=10 :
    print(x)
    x+=1
else:#Para executar um bloco de comandos se a condição do while não for satisfeita
    print('else')
    """
"""
print (list(range(0,10,1)))#esse trecho do código gera um intervalo de números de 0 a 9 de 1 em 1 e converte pra uma lista
print (list(range(10)))#faz a mesma coisa da linha acima
"""
"""
for c in range (10):
    print(c)
print()"""
"""
print(list(range(10,0,-1)))
for c in range(10,0,-1):
    print(c)
"""
"""
x = 0
while x < 10:
    x+=1
    if x%2 == 0:#Toda vez que essa condição for satisfeita o código ira pular o print e voltar para o while
        continue
    print(x)
print('Fim')
"""
i = 0
while i < 10:
    i+=1
    if i == 7:
        exit()#Finaliza a aplicação a partir daqui
    print(i)
print('Fim')
