from datetime import date

print('/' * 30)
print("Ano bixesto")
print('/' * 30)

ano = int(input('\n- Digite um ano qualquer para saber se ele é bissexto.\n'
                '- Digite 0 para ver o ano atual.\n'
                '>>> '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano bissexto.'.format(ano))

else:
    print('{} não é um ano bissexto.'.format(ano))