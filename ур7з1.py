N = int(input('Введите целое число:'))
a = []
print('Введите целые числа A(i) :')
for i in range(N):
   a.append(int(input()))
b = list(reversed(a))
print(b)


