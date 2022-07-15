num = int(input('Digite o número:'))

x = 0
y = 1

fibonacci = []
fibonacci.append(x)
fibonacci.append(y)
for i in range(10000):
    x =  x + y
    fibonacci.append(x)
    y = x + y
    fibonacci.append(y)

if fibonacci.count(num) > 0:
    print('O número informado pertence a sequencia fibonacci')
else:
    print('O número informado não pertence a sequencia fibonacci')


