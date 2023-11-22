import random
a = list()
a.append(random.random())
min = a[0]
max = a[0]
avg = a[0]

for i in range(9):
    a.append(random.random())
    avg += a[i + 1]
    if min > a[i + 1]:
        min = a[i + 1]
    if max < a[i + 1]:
        max = a[i + 1]

print("a = {}".format(a))
print("최댓값 : {}".format(max))
print("최솟값 : {}".format(min))
print("평균값 : {}".format(avg/10))