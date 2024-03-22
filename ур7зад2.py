N = int(input('Введите целое число:'))
tmp = []
print(f'Введите {N} чисел через пробел:')
tmp = list(map(int, input().split()))[:N]
a = tmp[-1]
tmp.pop()
tmp.insert(0, a)
print(tmp)

