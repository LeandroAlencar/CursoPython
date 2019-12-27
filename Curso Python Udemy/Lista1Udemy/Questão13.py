dias = int(input('digite a quantidade de dias: '))
horas = int(input('digite a quantidade de horas: '))
minutos = int(input('digite a quantidade de minutos: '))
seg = int(input('digite a quantidade de segundos:'))

conv = (dias*60*60*60)+(horas*60*60)+(minutos*60)+(seg)

print('O tempo digitado vale, em segundos: ',conv)