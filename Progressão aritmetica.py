a1 = int(input('Primeiro termo da razão: '))
r = int(input('Valor da razão (diferença entre o primeiro e segundo termo): '))
for n in range(1, 11):
    an = a1 + (n - 1) * r
    print(an, '->', end=' ')
print('Fim')