from math import hypot

print('+' * 30)
print("Cálculo de Hipotenusa")
print('+' * 30)

cat = float(input('digite o cateto: '))
cato = float(input('digite o cateto oposto: '))
hypo = hypot(cat, cato)
print('Cateto:{} \nCateto oposto:{} \nHipotenusa:{:.2f}'.format(cat, cato, hypo))
