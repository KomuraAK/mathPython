print('Me diga um múmero qualquer: ')

num = int(input('Digite um numero: '))
resultado = num % 2

if resultado == 0:
    print('o número é PAR')
else:
    print('o número é IMPAR')