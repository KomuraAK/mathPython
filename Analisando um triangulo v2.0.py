print('*' * 30)
print("Análise de Triângulo v2")
print('*' * 30)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Os valores FORMAM um triângulo!')
    if r1 == r2 == r3:
        print('Equilatero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isóceles') 
else:
    print('Os valores NÃO FORMAM um triângulo!')
