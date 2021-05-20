print('-' * 30)
print("Calculadora de descontos")
print('-' * 30)

preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100) # Para mudar a porcentagem, mexa no número 5

print('\nO produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))



