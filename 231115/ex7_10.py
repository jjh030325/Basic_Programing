import random

x = random.randrange(1, 21)
n = 0

while(True):
    inp = int(input("1이상 20이하의 수를 입력하세요 : "))
    n += 1
    if(x == inp):
        break
    elif(x > inp):
        print("입력이 x보다 더 작습니다.")
    else:
        print("입력이 x보다 더 큽니다.")


print("시도한 횟수 : {}".format(n))