print('+' * 30)
print('Reajuste salarial (+)\n')
print('+' * 30)
preço = float(input('Digite seu salário R$'))
novo = preço + (preço * 3/100) #Para escolher a porcentagem mude o 3

print('Seu salário de {:.2f} aumentando 3% foi para {:.2f}'.format(preço, novo))

