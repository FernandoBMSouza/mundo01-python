salario = float(input('Salario Atual: R$'))
aumento = 15
salarioComAumento = salario + (salario * aumento / 100)
print('Salário com {0} de aumento : R${1:.2f}'.format(
    aumento, salarioComAumento))
