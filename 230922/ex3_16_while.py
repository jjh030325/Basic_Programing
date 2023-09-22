n = int(input("1에서 9까지의 수를 입력하세요: "))
while True :
    if(n<=9 and n>0):
        break
    else:
        n = int(input("1에서 9까지의 수를 다시 입력하세요: "))

i = 1
while i<=9:
    print("{} * {} = {}".format(n, i, i*n))
    i+=1