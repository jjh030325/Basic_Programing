import random

lomio = random.randrange(1, 7)
juliet = random.randrange(1, 7)
print("로미오의 주사위 숫자는 {} 입니다.".format(lomio))
print("줄리엣의 주사위 숫자는 {} 입니다.".format(juliet))

if(lomio>juliet):
    print("로미오가 이겼습니다.")
elif(lomio<juliet):
    print("줄리엣이 이겼습니다.")
else:
    print("무승부입니다.")