preco = float(input('Preço: R$'))
desconto = 5
preco_descontado = preco - (preco * desconto / 100)
print('Preço com {0} de desconto : R${1:.2f}'.format(
    desconto, preco_descontado))
