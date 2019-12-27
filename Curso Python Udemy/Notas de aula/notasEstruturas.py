"""
lista = ['Magal',2,4,'Cfre',8,10]#è assim que criamos uma lista em python
print(lista)
print(lista[0])#Imprimindo o elemento de indice 0 da lista
lista2 = list((1,2,3,4,))#Para iterar uma lista de inteiros use dois parenteses e ponha a lista separada por virgulas no parenteses mais interno
print(lista2)
lista3 = [['a','b','c',],[0,1,4],[]]#Lista dentro da lista
print(lista3[0][1])
print(len(lista3))#A função len nos dá a quantidade de elementos da nossa lista
print(lista[-1])#Acessando o último elemento da lista com o comando lista[-1]
lista = lista + lista2 #Concatenando duas listas atraves do operador '+'
print(lista)
lista = [0,9,5] + lista #Concatenando duas listas, neste caso a lista a esquerda irá ocupar as primeiras posições de 'lista' 
print(lista)
"""
"""
lista = list((1,2,3,4,5))
lista.append(6)#Adicionando um elemento em lista através da função append
print(lista)
del(lista[-1])#Excluindo o último elemento da lista através da função del
print(lista)
#PERCORRENDO ITENS DE UMA LISTA:
for item in range(5):
    lista[item]+=10 #Acrescentando 10 a cada elemento da lista. use um range com um intervalo capaz de percorrer toda a lista
print(lista)
#Criando uma lista com range
listao = list(range(4,14,2))
print(listao)
#Uma forma mais adequada de percorrer uma lista(Essa é a mais bacana)
print()
for k in range(len(listao)):
    listao[k]+=10
print(listao)
"""
"""
#Percorrendo a lista com a função enumerated
lista = list(range(0,12,2))
for ind, item in enumerate(lista):
    lista[ind]+=10
print(lista)
"""
"""
#EXTRAINDO SUBLISTAS DENTRO DE UMA LISTA
lista = list(range(0,21))
print(lista)#printando toda a lista
print(lista[::2])#Printando do inicio até o fim de 2 em 2
print(lista[::-1])#Printando a lista ao contrario

#UMA APLICAÇÃO DE LISTAS, VERIFICANDO SE UMA PALAVRA É PALÍNDROMA
palavra = list(input('Digite uma palavra: '))
if palavra[::] == palavra[::-1]:
    print('A palavra digitada é palindroma')
else:
    print('A palavra digitada não é palindroma')


l = ['aaa','bbb', 'ccc']
l.insert(1,'ddd')#Insere a string ddd na posição 1 da lista
print(l)
l[2] = 'bbbb'#alterando o elemento 2 da nossa lista
print(l)
l.pop(2)#excluindo o elemento 2 da nossa lista
print(l) 
del(l[0:2])#Com a função del é possível excluir um dado intervalo da lista [start:stop:pass]
print(l)
"""
#Ordenamento de listas
lista = ['João', 'Marcos', 'Leandro', 'Israel', 'Henrique', 'Victor']
lista.reverse()#Inverte a leitura dos elementos da lista
print(lista)
lista.sort()#Já sabemos o que essa belezinha faz hehe
print(lista)
lista.sort(reverse=True)
print(lista)

print(len(lista))
i = lista.count('Marcos')#Devolve a quantidade de vezes que a string Marcos aparece na lista
print(i)
print(lista.index('Marcos'))#Devolve a posição na qual Marcos se encontra na lista
if ('Marcos' in lista):#Verificando se marcos está na lista
    print('Marcos está na lista')
else:
    print('Não tem Marcos na lista')