total = totmil = menor = cont = 0

barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    
    preco = float(input('Preço: R$ '))
    
    cont += 1
    
    total += preco
    
    if preco > 1000:
        total += 1
    
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    
    else:
        if preco < menor:
            menor = preco
            barato = produto
    
    resp = ' '
    while resp not in 'SN': 
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
    if resp == 'N':
        break

print('{:-^40}'.format('FIM DO SISTEMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')