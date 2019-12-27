"""
acao = int(input('Digite 1 para sim ou 2 para não:'))
if acao == 1:
    print('Você escolheu sim')
elif acao == 2:
    print('Você disse que não')
else:
    print('O número digitado não é igual a 1 nem igual a 2')


    ATÉ AGORA NADA DE NOVO

idade = int(input('Digite a sua idade: '))
if idade >= 18:
    print('Você é maior de idade!')
elif idade <= 0:
    print('Digite uma valor válido para a idade')
else:
    print('Você é menor de idade!')


    #TESTANDO OPERADORES LÓGICOS E RELACIONAIS
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 is num2:#is substituindo a igualdade
    print('O número %d é igual ao numero %d'%(num1,num2))
if num1 is not num2:# is not substinuido a desigualdade
    print('O número %d é diferente do numero %d'%(num1,num2))
if num1 < num2:
    print('O número', num1,'é menor que número', num2)
print(type(num1) is int)#Verificando se num1 é um número inteiro


a = 1000
if a > 0:
    print(a+a)
