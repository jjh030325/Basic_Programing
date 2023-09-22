n = int(input("1에서 9까지의 수를 입력하세요: "))
l = [1]
for i in l:
    if(n<=9 and n>0):
        break
    else:
        n = int(input("1에서 9까지의 수를 다시 입력하세요: "))
        l.append(i+1)

for i in range(1, 10):
    print("{} * {} = {}".format(n, i, i*n))