print('Digite dois números e será verificado qual é o maior')
num1 = int(input('Digite um número inteiro:'))
num2 = int(input('Digite um número inteiro:'))

if num1 < num2:
    print(num2,'>',num1)
elif num1 > num2:
    print(num2,'<',num1)
else:
    print(num1, '=', num2)