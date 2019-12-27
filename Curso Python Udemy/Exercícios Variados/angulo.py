#LENDO ÂNGULO E DEVOLVENDO SEN, COS E TAN
import math
ang = float(input('Digite o ângulo desejado: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(sen)
print('O seno do ângulo digitado é {0:.3f}' .format(sen))
print('O cosseno do ângulo digitado é {0:.3f}' .format(cos))
print('A tangente do ângulo digitado é {0:.3f}' .format(tan))