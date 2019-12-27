idade = int(input('Digite a sua idade: '))
if idade >= 18 and idade <100:
    print('Você é maior de idade')
if idade <= 0:
    print('Digite um valor válido para a idade! ')
if idade > 100 and idade <150:
    print('Nossa, você ainda está vivo?')
    exit()#encerra a aplicação aqui
if idade <18 and idade >0:
    print('Você é menor de idade')
else:
    print('Acho que você é velho demais para estar vivo')