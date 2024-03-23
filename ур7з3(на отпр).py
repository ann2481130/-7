m = int(input('Введите грузоподьёмность лодки m:'))
n = int(input('Введите число рыбаков:'))
a = []
print('Вес каждого рыбака n (<=m):')
for i in range(n):
   a.append(int(input()))
# сортировка по возрастанию веса
b = sorted(a)
# сортировка по убыванию
v = list(reversed(b))
if v[0] + v[1] <= m and  n%2 == 0 :
    cnt = int(n/2)
elif v[0] + v[1] <= m and  n%2 != 0 :
   cnt = int(n/2 + 1)
else:
    cnt = 0
    l = 0
    r = -1
    while len(v) > 0:
     if v[l] + v[r] >= m:
        v.pop(l)
        cnt += 1
        
     else:
        cnt += 1
        v.pop(l)
        v.pop(r)
print('Минимальное количество лодок:', cnt)
      
      

