n = int(input("Enter a value: "))
print('-' * 12)
i = 0
while (i <= 10):
    print('{} X {:2} = {}'.format(n, i, n * i))
    i = i + 1
print('-' * 12)