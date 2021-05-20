while True:
    n=int(input('\nDigite um número: '))
    if n<0: break
    for i in range(1, 11):
        print(f'{i:2} x {n} = {i*n}')
print('Fim do programa. Até a próxima!')

