import math
print('Desafio 018')
num = float(input('Digite um ângulo: '))
cos = math.cos(math.radians(num))
sin = math.sin(math.radians(num))
tan = math.tan(math.radians(num))
print('O ângulo {} tem: \nCoseno {:.2f} \nSeno {:.2f} \nTangente {:.2f}'.format(num, cos, sin, tan))

