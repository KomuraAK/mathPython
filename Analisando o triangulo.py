print('+' * 30)
print("Análise de Triângulo")
print('+' * 30)

print("\nDigite os valores do segmento.\n")

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Os valores FORMAM um triângulo!')
else:
    print('Os valores NÃO FORMAM um triângulo!')