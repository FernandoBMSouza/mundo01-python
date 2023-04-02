km = float(input('Km percorridos: '))
dias = int(input('Dias de aluguel: '))
preco = dias * 60 + km * 0.15
print('Total a pagar: R${0:.2f}'.format(preco))
