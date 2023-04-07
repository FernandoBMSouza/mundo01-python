nome = str(input('Digite seu nome: ')).strip()
dividido = nome.split()

print('Maiúsculo: ' + nome.upper())
print('Minúsculo: {}'.format(nome.lower()))
print('Quantidade de letras ao todo (sem contar espaços): {}'.format(
    len(nome) - nome.count(' ')))
print('Quantidade de letras do primeiro nome: {}'.format(len(dividido[0])))
